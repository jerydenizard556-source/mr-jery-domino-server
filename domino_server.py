import os, json, random, string, asyncio
from dataclasses import dataclass, field
from typing import Any
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title='MR_Jery Domino Online Server', version='1.0.0')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])

@dataclass
class Player:
    ws: WebSocket
    name: str
    pid: str
    hand: list[dict] = field(default_factory=list)
    connected: bool = True

@dataclass
class Room:
    code: str
    max_players: int
    players: list[Player] = field(default_factory=list)
    stock: list[dict] = field(default_factory=list)
    chain: list[dict] = field(default_factory=list)
    left: int | None = None
    right: int | None = None
    turn: int = 0
    passes: int = 0
    started: bool = False
    over: bool = False
    lock: asyncio.Lock = field(default_factory=asyncio.Lock)

rooms: dict[str, Room] = {}

def new_code():
    alphabet = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(random.choice(alphabet) for _ in range(6))
        if code not in rooms: return code

def make_set():
    tiles=[]; i=0
    for a in range(7):
        for b in range(a,7):
            tiles.append({'id':f'd{i}', 'a':a, 'b':b}); i+=1
    random.shuffle(tiles)
    return tiles

def can_play(tile, room):
    if not room.chain: return True
    return tile['a'] in (room.left, room.right) or tile['b'] in (room.left, room.right)

def public_state(room, recipient: Player | None = None):
    players=[]
    for p in room.players:
        players.append({'id':p.pid,'name':p.name,'tile_count':len(p.hand),'connected':p.connected,
                        'hand':p.hand if recipient and p.pid == recipient.pid else None})
    return {'type':'state','room':room.code,'max_players':room.max_players,'players':players,
            'chain':room.chain,'left':room.left,'right':room.right,'stock_count':len(room.stock),
            'turn_player_id':room.players[room.turn].pid if room.players and room.turn < len(room.players) else None,
            'started':room.started,'over':room.over,'passes':room.passes}

async def send_json(ws, data):
    await ws.send_text(json.dumps(data, ensure_ascii=False))

async def broadcast(room, event=None):
    for p in list(room.players):
        if p.connected:
            try:
                await send_json(p.ws, public_state(room,p))
                if event: await send_json(p.ws,event)
            except Exception:
                p.connected=False

async def error(ws, message):
    await send_json(ws, {'type':'error','message':message})

@app.get('/')
def root():
    return {'ok':True,'service':'MR_Jery Domino Online Server','version':'1.0.0','websocket':'/ws','rooms':len(rooms)}

@app.get('/health')
def health():
    return {'ok':True,'service':'domino','rooms':len(rooms)}

@app.websocket('/ws')
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    me: Player | None = None
    room: Room | None = None
    try:
        while True:
            raw = await ws.receive_text()
            try: data=json.loads(raw)
            except json.JSONDecodeError:
                await error(ws,'Mesaj JSON la pa valab.'); continue
            action=str(data.get('type','')).lower()
            if action == 'create_room':
                if me: await error(ws,'Ou deja nan yon chanm.'); continue
                max_players=max(2,min(4,int(data.get('max_players',2))))
                name=str(data.get('name') or 'Jwè 1')[:24].strip() or 'Jwè 1'
                code=new_code(); room=Room(code=code,max_players=max_players)
                me=Player(ws=ws,name=name,pid='p'+''.join(random.choices(string.ascii_lowercase+string.digits,k=10)))
                room.players.append(me); rooms[code]=room
                await send_json(ws,{'type':'room_created','room':code,'player_id':me.pid})
                await broadcast(room,{'type':'notice','message':f'{name} kreye chanm nan.'})
            elif action == 'join_room':
                if me: await error(ws,'Ou deja nan yon chanm.'); continue
                code=str(data.get('room','')).strip().upper(); target=rooms.get(code)
                if not target: await error(ws,'Chanm sa a pa egziste ankò.'); continue
                if target.started or len(target.players)>=target.max_players: await error(ws,'Chanm nan deja plen oswa pati a kòmanse.'); continue
                name=str(data.get('name') or f'Jwè {len(target.players)+1}')[:24].strip() or 'Jwè'
                room=target; me=Player(ws=ws,name=name,pid='p'+''.join(random.choices(string.ascii_lowercase+string.digits,k=10)))
                room.players.append(me)
                await send_json(ws,{'type':'room_joined','room':code,'player_id':me.pid})
                await broadcast(room,{'type':'notice','message':f'{name} antre nan chanm nan.'})
            elif action == 'start_game':
                if not room or not me: await error(ws,'Kreye oswa antre nan yon chanm anvan.'); continue
                async with room.lock:
                    if room.started: await error(ws,'Pati a deja kòmanse.'); continue
                    if len(room.players)<2: await error(ws,'Omwen 2 jwè nesesè.'); continue
                    tiles=make_set(); random.shuffle(room.players)
                    for p in room.players: p.hand=[]
                    for _ in range(7):
                        for p in room.players: p.hand.append(tiles.pop())
                    room.stock=tiles; room.chain=[]; room.left=room.right=None; room.turn=0; room.passes=0; room.over=False; room.started=True
                    await broadcast(room,{'type':'notice','message':'Pati a kòmanse! Chak jwè resevwa 7 domino.'})
            elif action in ('play_tile','move'):
                if not room or not me or not room.started or room.over: await error(ws,'Pa gen pati aktif.'); continue
                async with room.lock:
                    if room.players[room.turn].pid != me.pid: await error(ws,'Se pa tou pa ou.'); continue
                    tile_id=str(data.get('tile_id',data.get('id','')))
                    side=str(data.get('side','left')).lower()
                    tile=next((t for t in me.hand if t['id']==tile_id),None)
                    if not tile: await error(ws,'Domino sa a pa nan men ou.'); continue
                    if not can_play(tile,room): await error(ws,'Domino sa a pa mache ak pwent tablo a.'); continue
                    me.hand.remove(tile)
                    placed=dict(tile)
                    if not room.chain:
                        room.chain.append(placed); room.left=tile['a']; room.right=tile['b']
                    elif side=='left':
                        if tile['b']==room.left: placed={'id':tile['id'],'a':tile['a'],'b':tile['b']}
                        elif tile['a']==room.left: placed={'id':tile['id'],'a':tile['b'],'b':tile['a']}
                        else: await error(ws,'Pyès la pa mache agoch.'); me.hand.append(tile); continue
                        room.chain.insert(0,placed); room.left=placed['a']
                    else:
                        if tile['a']==room.right: placed={'id':tile['id'],'a':tile['a'],'b':tile['b']}
                        elif tile['b']==room.right: placed={'id':tile['id'],'a':tile['b'],'b':tile['a']}
                        else: await error(ws,'Pyès la pa mache adwat.'); me.hand.append(tile); continue
                        room.chain.append(placed); room.right=placed['b']
                    room.passes=0
                    if not me.hand:
                        room.over=True
                        await broadcast(room,{'type':'game_over','winner_id':me.pid,'winner':me.name,'reason':'empty_hand','message':f'{me.name} genyen! Li fini tout domino li yo.'})
                    else:
                        room.turn=(room.turn+1)%len(room.players)
                        await broadcast(room,{'type':'tile_played','player_id':me.pid,'tile':placed,'side':side})
            elif action == 'draw':
                if not room or not me or not room.started or room.over: await error(ws,'Pa gen pati aktif.'); continue
                async with room.lock:
                    if room.players[room.turn].pid != me.pid: await error(ws,'Se pa tou pa ou.'); continue
                    if any(can_play(t,room) for t in me.hand): await error(ws,'Ou gen domino ki ka jwe; chwazi youn.'); continue
                    if not room.stock: await error(ws,'Pa rete domino pou rale; ou ka pase tou.'); continue
                    me.hand.append(room.stock.pop())
                    await broadcast(room,{'type':'tile_drawn','player_id':me.pid})
            elif action == 'pass':
                if not room or not me or not room.started or room.over: await error(ws,'Pa gen pati aktif.'); continue
                async with room.lock:
                    if room.players[room.turn].pid != me.pid: await error(ws,'Se pa tou pa ou.'); continue
                    if any(can_play(t,room) for t in me.hand): await error(ws,'Ou gen domino ki ka jwe; ou pa ka pase.'); continue
                    if room.stock: await error(ws,'Rale domino anvan ou pase.'); continue
                    room.passes+=1
                    if room.passes>=len(room.players):
                        scores=[(sum(t['a']+t['b'] for t in p.hand),p) for p in room.players]
                        low=min(x[0] for x in scores); winners=[p.name for score,p in scores if score==low]
                        room.over=True
                        await broadcast(room,{'type':'game_over','winner':', '.join(winners),'reason':'blocked','message':'Pati bloke. Gayan: '+', '.join(winners)})
                    else:
                        room.turn=(room.turn+1)%len(room.players)
                        await broadcast(room,{'type':'passed','player_id':me.pid,'player_name':me.name})
            elif action == 'chat':
                if not room or not me: await error(ws,'Ou pa nan yon chanm.'); continue
                msg=str(data.get('message','')).strip()[:300]
                if msg: await broadcast(room,{'type':'chat','player_id':me.pid,'name':me.name,'message':msg})
            elif action == 'leave_room':
                if room and me:
                    await disconnect_player(room,me)
                    room=None; me=None
                await send_json(ws,{'type':'left_room'})
            elif action == 'ping':
                await send_json(ws,{'type':'pong'})
            else:
                await error(ws,'Aksyon sa a pa rekonèt.')
    except WebSocketDisconnect:
        pass
    except Exception as exc:
        try: await error(ws,'Erè sèvè. Eseye rekonekte.'); print('WebSocket error:',repr(exc))
        except Exception: pass
    finally:
        if room and me: await disconnect_player(room,me)

async def disconnect_player(room: Room, player: Player):
    player.connected=False
    if player in room.players:
        # Keep the room alive for a short reconnect window; do not expose disconnected player's hand to others.
        await broadcast(room,{'type':'notice','message':f'{player.name} dekonekte.'})
        if all(not p.connected for p in room.players):
            rooms.pop(room.code,None)

if __name__ == '__main__':
    port=int(os.environ.get('PORT','10000'))
    uvicorn.run('domino_server:app',host='0.0.0.0',port=port)
