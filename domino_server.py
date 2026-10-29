import os
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse

app = FastAPI(title="MR_Jery Game Server")

connections = set()


@app.get("/")
async def home():
    return {
        "ok": True,
        "service": "MR_Jery Game Server",
        "status": "running"
    }


@app.get("/health")
async def health():
    return JSONResponse({
        "ok": True,
        "status": "healthy"
    })


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.add(websocket)

    try:
        await websocket.send_json({
            "type": "connected",
            "message": "Koneksyon ak sèvè a reyisi."
        })

        while True:
            message = await websocket.receive_text()

            # Voye mesaj la bay lòt kliyan ki konekte yo.
            disconnected = []

            for client in list(connections):
                if client == websocket:
                    continue

                try:
                    await client.send_text(message)
                except Exception:
                    disconnected.append(client)

            for client in disconnected:
                connections.discard(client)

    except WebSocketDisconnect:
        pass

    finally:
        connections.discard(websocket)


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", "10000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
