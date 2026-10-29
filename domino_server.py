<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MR JERY MOPION</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #111827;
    color: white;
    font-family: Arial, sans-serif;
    min-height: 100vh;
}

.app {
    width: 100%;
    max-width: 900px;
    margin: auto;
    padding: 20px 12px;
    text-align: center;
}

h1 {
    margin: 8px 0;
    font-size: 28px;
}

.screen {
    display: none;
}

.screen.active {
    display: block;
}

/* MENU */

.main-menu {
    max-width: 380px;
    margin: 45px auto;
    display: flex;
    flex-direction: column;
    gap: 14px;
}

.menu-button {
    width: 100%;
    padding: 16px;
    border: 1px solid #374151;
    border-radius: 10px;
    background: #273449;
    color: white;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
}

.menu-button:hover {
    background: #374151;
}

.back-button,
.action-button {
    margin-top: 10px;
    padding: 11px 20px;
    border: 1px solid #4B5563;
    border-radius: 8px;
    background: #1F2937;
    color: white;
    font-size: 15px;
    cursor: pointer;
}

.action-button {
    margin: 5px;
    background: #273449;
}

.action-button:disabled {
    opacity: 0.45;
    cursor: not-allowed;
}

/* ONLINE MENU */

.online-box {
    max-width: 380px;
    margin: 30px auto;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.online-choice {
    width: 100%;
    padding: 16px;
    border-radius: 10px;
    font-size: 17px;
    font-weight: bold;
    background: #273449;
    color: white;
    border: 1px solid #374151;
    cursor: pointer;
}

.online-choice:hover {
    background: #374151;
}

.friend-box {
    display: none;
    max-width: 350px;
    margin: 20px auto;
    padding: 16px;
    border: 1px solid #374151;
    border-radius: 10px;
    background: #1F2937;
}

.friend-box.show {
    display: block;
}

.friend-box input {
    width: 100%;
    padding: 13px;
    border-radius: 8px;
    font-size: 17px;
    background: white;
    color: #111;
    border: 1px solid #555;
    text-align: center;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.friend-box button {
    width: 100%;
    padding: 13px;
    border-radius: 8px;
    font-size: 16px;
    background: #273449;
    color: white;
    border: 1px solid #374151;
    cursor: pointer;
    margin-top: 7px;
}

.searching-box {
    display: none;
    max-width: 380px;
    margin: 30px auto;
    padding: 18px;
    border: 1px solid #D4AF37;
    border-radius: 10px;
    background: #1F2937;
}

.searching-box.show {
    display: block;
}

.searching-message {
    color: #D4AF37;
    font-weight: bold;
    font-size: 17px;
    margin-bottom: 12px;
}

.cancel-search {
    padding: 11px 20px;
    border-radius: 8px;
    background: #991B1B;
    color: white;
    border: 1px solid #7F1D1D;
    cursor: pointer;
    font-weight: bold;
}

/* ROOM */

.room {
    color: #D4AF37;
    font-weight: bold;
    margin-top: 15px;
}

/* INFORMATIONS */

.game-info {
    margin: 10px auto 12px;
    font-size: 16px;
}

.status {
    color: #D1D5DB;
    margin: 5px 0;
}

.error {
    color: #F87171;
    margin-top: 10px;
}

/* TIMER */

.timers {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
    margin: 10px auto 14px;
}

.player-timer {
    min-width: 125px;
    padding: 9px 14px;
    border: 1px solid #374151;
    border-radius: 9px;
    background: #1F2937;
    font-weight: bold;
    font-size: 16px;
}

.player-timer.active {
    border-color: #D4AF37;
    color: #D4AF37;
}

.player-timer.warning {
    color: #F87171;
    border-color: #F87171;
}

.timer-label {
    display: block;
    font-size: 12px;
    margin-bottom: 3px;
    color: #D1D5DB;
}

.timer-value {
    font-size: 21px;
}

/* SCORE */

.score-board {
    display: flex;
    justify-content: center;
    gap: 25px;
    flex-wrap: wrap;
    margin: 8px auto 12px;
    font-size: 17px;
    font-weight: bold;
}

.score-player {
    padding: 7px 14px;
    border: 1px solid #374151;
    border-radius: 8px;
    background: #1F2937;
}

.score-player span {
    color: #D4AF37;
    font-size: 20px;
}

/* ACTIONS */

.game-actions {
    margin: 8px auto;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 5px;
}

/* REJWE */

.rematch-box {
    max-width: 600px;
    width: 100%;
    min-height: 94px;
    height: 94px;
    margin: 12px auto;
    padding: 8px 12px;
    border: 1px solid #D4AF37;
    border-radius: 9px;
    background: #1F2937;
    display: flex;
    flex-direction: column;
    justify-content: center;
    visibility: hidden;
    overflow: hidden;
    box-sizing: border-box;
}

/* Zòn revanche a rete konpak pou revèy yo ak tablo a rete vizib ansanm. */
#rematchBox { min-height: 58px; height: 58px; margin: 5px auto 6px; padding: 4px 8px; }
#undoBox { min-height: 58px; height: 58px; margin: 5px auto 6px; padding: 4px 8px; }
#rematchBox .rematch-button, #undoBox .rematch-button { min-height: 36px; padding: 6px 12px; font-size: 14px; }
#rematchBox .rematch-message, #undoBox .rematch-message { margin: 1px 0 4px; font-size: 13px; line-height: 1.2; }
#onlineBlackTimer, #onlineRedTimer { margin: 3px 0; }
#onlineBoard { margin-top: -8px !important; margin-bottom: 10px !important; }
#onlineBoard .cell.last-move-cell { z-index: 8; }
#onlineBoard .stone.last-move-stone { width: 100%; height: 100%; flex-basis: 100%; transform: scale(1.14); transform-origin: center; box-shadow: 0 0 0 3px #facc15, 0 0 10px rgba(250,204,21,1); z-index: 12; }
@media (max-width: 600px) {
  #rematchBox, #undoBox { min-height: 50px; height: 50px; }
  #rematchBox .rematch-button, #undoBox .rematch-button { min-height: 32px; padding: 5px 9px; font-size: 12px; }
  #onlineBoard { width: min(98vw, 760px); margin-top: -8px !important; }
}
#rematchBox.show, #undoBox.show { visibility: visible; }
#onlineStatus { min-height: 34px; display: flex; align-items: center; justify-content: center; }
#onlineStatus.opponent-turn { font-size: 22px; font-weight: 900; color: #FBBF24; }
#onlineMatchNotice { min-height: 28px; }
#onlineBoard { contain: layout paint; }
#rematchBox .rematch-button, #undoBox .rematch-button { min-height: 46px; padding: 11px 18px; font-size: 16px; }

.rematch-box.show {
    visibility: visible;
}

.online-match-notice {
    min-height: 28px;
    margin: 4px auto 6px;
    color: #D4AF37;
    font-weight: bold;
}

.spectator-count {
    color: #D1D5DB;
    font-size: 14px;
    margin: 5px 0 8px;
}

.spectator-box {
    max-width: 600px;
    margin: 25px auto;
}

.live-match-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 15px;
}

.live-match-button {
    width: 100%;
    padding: 14px;
    border: 1px solid #374151;
    border-radius: 10px;
    background: #273449;
    color: white;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
}

.live-match-button:hover {
    background: #374151;
}

.live-empty {
    padding: 15px;
    color: #D1D5DB;
    border: 1px solid #374151;
    border-radius: 10px;
    background: #1F2937;
}

.rematch-message {
    color: #D4AF37;
    font-weight: bold;
    margin-bottom: 10px;
}

.rematch-actions {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 8px;
}

.rematch-button {
    padding: 10px 18px;
    border-radius: 8px;
    border: 1px solid #4B5563;
    color: white;
    cursor: pointer;
    font-weight: bold;
}

.rematch-accept {
    background: #166534;
}

.rematch-refuse {
    background: #991B1B;
}

.rematch-request {
    background: #273449;
}

/* RESULTAT ONLINE */

.online-result {
    display: none;
    margin: 12px auto;
    padding: 12px;
    max-width: 600px;
    border: 1px solid #D4AF37;
    border-radius: 9px;
    color: #D4AF37;
    font-weight: bold;
    font-size: 18px;
}

.online-result.show {
    display: block;
}

/* TABLEAU */

.board-area {
    width: min(96vw, 760px);
    max-width: 100%;
    box-sizing: border-box;
    margin: 20px auto;
    display: grid;
    grid-template-columns: clamp(18px, 4vw, 30px) minmax(0, 1fr);
    grid-template-rows: clamp(18px, 4vw, 30px) minmax(0, 1fr);
    aspect-ratio: 1 / 1;
    background: #f8fafc;
    border: clamp(2px, 0.45vw, 5px) solid #b7bec8;
    border-radius: 8px;
    padding: clamp(2px, 0.35vw, 4px);
    overflow: hidden;
}
.board-area > * { min-width: 0; min-height: 0; }
.board-area .board { width: 100%; height: 100%; max-width: 100%; aspect-ratio: 1 / 1; }
.board-area .letters, .board-area .numbers { min-width: 0; min-height: 0; overflow: hidden; }
.board-area .letters span, .board-area .numbers span { min-width: 0; text-align: center; font-size: clamp(7px, 1.3vw, 12px); line-height: 1; color: #172033; }
.board-area .letters span { font-weight: 800; }
.board-area .numbers span { font-weight: 700; }

.letters {
    grid-column: 2;
    display: grid;
    grid-template-columns: repeat(20, 1fr);
    align-items: center;
    justify-items: center;
    font-size: 12px;
    font-weight: bold;
    color: #111;
}

.numbers {
    grid-row: 2;
    display: grid;
    grid-template-rows: repeat(20, 1fr);
    align-items: center;
    justify-items: center;
    font-size: 12px;
    font-weight: bold;
    color: #111;
}

.board {
    grid-column: 2;
    grid-row: 2;
    position: relative;
    display: grid;
    grid-template-columns: repeat(20, minmax(0, 1fr));
    grid-template-rows: repeat(20, minmax(0, 1fr));
    width: 100%;
    aspect-ratio: 1 / 1;
    min-width: 0;
    min-height: 0;
    overflow: hidden;
}

.cell {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
    min-width: 0;
    min-height: 0;
    cursor: pointer;
    overflow: hidden;
}

/* Grille robuste: chaque case dessine deux demi-lignes qui se rejoignent
   exactement au centre de l'intersection. Fonctionne aussi sur mobile. */
.board {
    background-color: #f8fafc !important;
    background-image: none !important;
}
.board .cell {
    position: relative;
    z-index: 1;
    background-color: transparent !important;
    background-image:
      linear-gradient(to right, transparent calc(50% - 0.8px), #334155 calc(50% - 0.8px), #334155 calc(50% + 0.8px), transparent calc(50% + 0.8px)),
      linear-gradient(to bottom, transparent calc(50% - 0.8px), #334155 calc(50% - 0.8px), #334155 calc(50% + 0.8px), transparent calc(50% + 0.8px));
    background-repeat: no-repeat;
}
.board .stone { position: relative; z-index: 5; }

/* PIONS */

.stone {
    width: 74%;
    height: 74%;
    flex: 0 0 74%;
    border-radius: 50%;
    position: relative;
    z-index: 5;
}

.black {
    background: #111111;
}

.red {
    background: #DC2626;
}

/* LIGNE VICTOIRE */

.winning-line-svg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 20;
    pointer-events: none;
}

.winning-line-svg line {
    stroke: #D4AF37;
    stroke-width: 4;
    stroke-linecap: round;
}

/* VICTOIRE */

.win-title {
    font-size: 34px;
    margin-top: 60px;
}

.win-message {
    font-size: 21px;
    color: #D4AF37;
    font-weight: bold;
    margin: 25px 0;
}

.win-buttons {
    max-width: 380px;
    margin: 25px auto;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.undo-box {
    margin-top: 12px;
}

.undo-button {
    border: none;
    border-radius: 10px;
    padding: 10px 16px;
    font-size: 15px;
    font-weight: bold;
    cursor: pointer;
    margin: 4px;
}

.undo-request {
    background: #2563EB;
    color: #FFFFFF;
}

.undo-accept {
    background: #16A34A;
    color: #FFFFFF;
}

.undo-refuse {
    background: #DC2626;
    color: #FFFFFF;
}

/* MOBILE */

@media (max-width: 500px) {

    .app {
        padding: 12px 6px;
    }

    h1 {
        font-size: 24px;
    }

    .main-menu {
        margin: 35px auto;
        padding: 0 10px;
    }

    .menu-button {
        font-size: 16px;
        padding: 15px;
    }

    .board-area {
        width: min(calc(100vw - 18px), 760px);
        grid-template-columns: 18px minmax(0, 1fr);
        grid-template-rows: 18px minmax(0, 1fr);
        border-width: 2px;
        padding: 2px;
        margin: 12px auto;
    }
    .board-area .letters span, .board-area .numbers span { font-size: clamp(6px, 1.8vw, 8px); }

    .letters,
    .numbers {
        font-size: 9px;
    }

    .stone {
        width: 68%;
    }

    .action-button {
        font-size: 13px;
        padding: 9px 12px;
    }

    .player-timer {
        min-width: 115px;
        padding: 8px 10px;
    }

    .timer-value {
        font-size: 19px;
    }

    .score-board {
        gap: 8px;
        font-size: 14px;
    }

    .score-player {
        padding: 6px 10px;
    }

    .score-player span {
        font-size: 18px;
    }

    .rematch-button {
        font-size: 13px;
        padding: 9px 13px;
    }

    .online-choice {
        font-size: 15px;
    }

    .win-title {
        font-size: 28px;
    }

    .win-message {
        font-size: 18px;
    }
}

    /* ==================================================
       COMPTE / MENU JOUEUR
    ================================================== */

    .account-box,
    .profile-box,
    .settings-box,
    .waiting-box,
    .spectator-box {
        max-width: 420px;
        margin: 22px auto;
        padding: 20px;
        border: 1px solid #374151;
        border-radius: 14px;
        background: #1F2937;
        box-sizing: border-box;
    }

    .account-box h2 {
        margin: 8px 0 14px;
        color: #D4AF37;
    }

    .account-box input,
    .spectator-box input {
        width: 100%;
        box-sizing: border-box;
        margin: 7px 0;
        padding: 12px 14px;
        border: 1px solid #4B5563;
        border-radius: 9px;
        background: #111827;
        color: #F9FAFB;
        outline: none;
    }

    .account-button {
        width: 100%;
        margin-top: 8px;
        padding: 12px;
        border: 1px solid #D4AF37;
        border-radius: 9px;
        background: #374151;
        color: #F9FAFB;
        font-weight: bold;
        cursor: pointer;
    }

    .account-button:hover {
        background: #4B5563;
    }

    .account-separator {
        height: 1px;
        background: #374151;
        margin: 22px 0;
    }

    .account-status {
        min-height: 24px;
        margin-top: 12px;
        color: #D1D5DB;
        text-align: center;
    }

    .account-user,
    .account-user-menu {
        max-width: 420px;
        margin: 15px auto;
        padding: 12px;
        border: 1px solid #D4AF37;
        border-radius: 10px;
        background: #1F2937;
        color: #D4AF37;
        font-weight: bold;
        text-align: center;
        box-sizing: border-box;
    }

    .account-menu-list {
        margin: 25px auto;
    }

    .logout-button {
        background: #7F1D1D !important;
        border-color: #991B1B !important;
    }

    .logout-button:hover {
        background: #991B1B !important;
    }

    .profile-row {
        padding: 12px 0;
        border-bottom: 1px solid #374151;
    }

    .profile-row:last-child {
        border-bottom: none;
    }

    .profile-label {
        display: block;
        color: #9CA3AF;
        font-size: 13px;
        margin-bottom: 4px;
    }

    .profile-value {
        font-size: 17px;
        font-weight: bold;
        word-break: break-word;
    }

    .settings-box {
        text-align: center;
        color: #D1D5DB;
        line-height: 1.5;
    }

    .waiting-list {
        text-align: left;
        margin: 15px 0;
    }

    .waiting-player {
        padding: 12px;
        margin: 8px 0;
        border-radius: 9px;
        background: #111827;
        border: 1px solid #374151;
    }

    .spectator-count {
        margin: 10px auto;
        padding: 9px 12px;
        border-radius: 9px;
        background: #1F2937;
        color: #D4AF37;
        font-weight: bold;
        text-align: center;
    }


.online-players-box{max-width:600px;margin:16px auto;padding:16px;border:1px solid #374151;border-radius:12px;background:#1F2937}.online-players-title{color:#D4AF37;font-weight:bold;text-align:center;margin-bottom:10px}.online-players-list{display:flex;flex-direction:column;gap:8px}.online-player-row{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 12px;border-radius:9px;background:#111827;border:1px solid #374151}.online-player-name{min-width:0;color:#F9FAFB;font-weight:bold;overflow-wrap:anywhere}.online-player-state{color:#86EFAC;font-size:12px;margin-left:6px}.online-player-invite{padding:8px 12px;border-radius:8px;border:1px solid #D4AF37;background:#273449;color:#F9FAFB;font-weight:bold;cursor:pointer}.online-player-invite:disabled{opacity:.5;cursor:not-allowed}.online-players-status{color:#9CA3AF;text-align:center;font-size:13px;margin-top:9px}.game-invite-box{display:none;position:fixed;top:16px;left:50%;transform:translateX(-50%);z-index:99999;width:calc(100% - 28px);max-width:600px;margin:0;padding:14px;border:1px solid #D4AF37;border-radius:12px;background:#1F2937;text-align:center;box-shadow:0 12px 36px rgba(0,0,0,.45)}.game-invite-message{color:#D4AF37;font-weight:bold;margin-bottom:10px}.game-invite-actions{display:flex;justify-content:center;gap:8px;flex-wrap:wrap}.game-invite-actions button{padding:10px 18px;border-radius:8px;border:1px solid #4B5563;color:white;font-weight:bold;cursor:pointer}.invite-accept{background:#166534}.invite-refuse{background:#991B1B}

/* ==================================================
   WALLET / DEFIS — PREPARATION
   Mode test: aucune vraie transaction n'est exécutée
================================================== */
.wallet-box,.bet-box,.admin-box{max-width:650px;margin:16px auto;padding:18px;border:1px solid #374151;border-radius:14px;background:#1F2937;text-align:left}.wallet-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px}.wallet-card{padding:16px;border-radius:12px;background:#111827;border:1px solid #374151}.wallet-card small{display:block;color:#9CA3AF}.wallet-card strong{display:block;font-size:25px;margin-top:6px;color:#D4AF37}.wallet-actions,.bet-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}.wallet-actions button,.bet-actions button{flex:1;min-width:150px;padding:11px;border-radius:9px;border:1px solid #4B5563;color:white;background:#273449;font-weight:bold;cursor:pointer}.primary-pay{background:#166534!important;border-color:#22C55E!important}.danger-pay{background:#7F1D1D!important}.form-row{display:grid;grid-template-columns:1fr 1fr;gap:10px}.form-row input,.form-row select,.bet-box input,.bet-box select{width:100%;padding:11px;border-radius:9px;border:1px solid #4B5563;background:#111827;color:white}.notice-test{padding:12px;border-radius:10px;background:#422006;border:1px solid #D97706;color:#FED7AA;margin-bottom:12px;font-size:13px}.calc-box{margin-top:14px;padding:14px;border-radius:10px;background:#111827;border:1px solid #374151;line-height:1.8}.history-item{padding:10px;border-bottom:1px solid #374151;color:#D1D5DB}.history-item:last-child{border-bottom:0}.admin-stat{font-size:28px;color:#D4AF37;font-weight:bold}.@media(max-width:600px){.form-row{grid-template-columns:1fr}}


/* ==================================================
   MR_JERY LANDING / AUTH REDESIGN
================================================== */
body{background:#030916;color:#fff;font-family:Inter,Segoe UI,Arial,sans-serif;overflow-x:hidden}.app{max-width:none;padding:0}.screen{min-height:100vh}.landing-shell{min-height:100vh;background:radial-gradient(circle at 50% 35%,rgba(0,91,180,.25),transparent 38%),linear-gradient(135deg,#020711,#071426 55%,#020711);position:relative;overflow:hidden}.landing-shell:before{content:"";position:absolute;inset:0;background:linear-gradient(120deg,transparent 0 38%,rgba(240,174,31,.12) 39%,transparent 41% 62%,rgba(0,128,255,.12) 63%,transparent 66%);pointer-events:none}.landing-header{height:76px;border-bottom:1px solid rgba(91,157,224,.3);display:flex;align-items:center;padding:0 34px;gap:28px;position:relative;z-index:5;background:rgba(2,7,17,.72);backdrop-filter:blur(14px)}.brand-mini{font-weight:800;font-size:22px;display:flex;align-items:center;gap:9px;white-space:nowrap}.brand-mini b{color:#f5b92e}.brand-crown{color:#f5b92e;font-size:30px;text-shadow:0 0 18px rgba(245,185,46,.35)}.landing-nav{display:flex;gap:8px;margin:auto}.nav-link{background:none;border:0;color:#c9d4e8;padding:13px 17px;border-bottom:2px solid transparent;cursor:pointer;font-weight:700}.nav-link.active,.nav-link:hover{color:#f5c13a;border-bottom-color:#f5c13a}.language-wrap{position:relative}.language-button{height:45px;padding:0 16px;border:1px solid #2494ed;border-radius:10px;background:#07172b;color:#fff;font-weight:700;font-size:14px;cursor:pointer;display:flex;align-items:center;gap:9px}.language-menu{display:none;position:absolute;right:0;top:52px;width:190px;background:#07172b;border:1px solid #238ddd;border-radius:10px;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.45);z-index:20}.language-menu.show{display:block}.language-menu button{display:block;width:100%;padding:12px 14px;border:0;background:transparent;color:#fff;text-align:left;cursor:pointer}.language-menu button:hover{background:#0c65b6}.landing-hero{min-height:calc(100vh - 76px);display:grid;grid-template-columns:minmax(330px,1fr) minmax(420px,1fr);align-items:center;gap:20px;padding:55px 8%;position:relative;z-index:1}.world-map{position:absolute;inset:0;opacity:.2;background-image:radial-gradient(circle,#1684e8 1.4px,transparent 1.4px);background-size:12px 12px;mask-image:radial-gradient(ellipse at 50% 42%,#000 0 42%,transparent 70%)}.hero-logo{text-align:center;position:relative;z-index:1;filter:drop-shadow(0 20px 35px rgba(0,0,0,.55))}.logo-crown{font-size:92px;line-height:.8;color:#f7bf37;text-shadow:0 0 25px rgba(247,191,55,.45)}.logo-ring{width:280px;height:190px;margin:-5px auto -30px;border:9px solid #e9a927;border-radius:50% 50% 42% 42%;background:radial-gradient(circle,#172337,#03070e 70%);box-shadow:inset 0 0 0 3px #7d5a16,0 0 35px rgba(241,174,30,.25);display:flex;align-items:center;justify-content:center}.logo-board-mini{width:130px;height:105px;display:grid;grid-template-columns:repeat(3,1fr);gap:7px;padding:10px;background:linear-gradient(90deg,transparent 48%,#d9a52e 49% 51%,transparent 52%),linear-gradient(0deg,transparent 48%,#d9a52e 49% 51%,transparent 52%);border:2px solid #d9a52e}.logo-board-mini i{width:22px;height:22px;border-radius:50%;background:#f3f5f8;box-shadow:0 3px 8px #000}.logo-board-mini i:nth-child(even){background:#101820}.logo-title{margin-top:0;font-size:54px;font-weight:900;line-height:.88;letter-spacing:-2px;text-transform:uppercase}.logo-title span{display:block;color:#f1f3f7;text-shadow:4px 4px 0 #111,0 0 20px rgba(255,255,255,.15)}.logo-title strong{display:block;color:#f5b92e;text-shadow:3px 4px 0 #111}.hero-copy{position:relative;z-index:2;max-width:650px}.hero-copy h1{font-size:44px;line-height:1.08;margin:0 0 18px}.hero-copy h1 em{color:#f5bb31;font-style:normal}.hero-copy p{font-size:20px;line-height:1.6;color:#d5deec;max-width:610px}.hero-features{display:flex;flex-wrap:wrap;gap:14px 20px;margin:26px 0;color:#dbe5f2}.hero-features span{display:flex;gap:7px;align-items:center}.hero-features b{font-size:14px}.hero-actions{display:flex;gap:15px;flex-wrap:wrap;margin-top:26px}.hero-btn{border-radius:34px;padding:16px 28px;font-size:16px;font-weight:900;cursor:pointer;min-width:220px;border:1px solid #6d88a8;display:flex;justify-content:center;align-items:center;gap:10px}.hero-btn.gold{background:linear-gradient(180deg,#ffd34e,#e8a90e);color:#10151d;border:0;box-shadow:0 10px 30px rgba(240,176,28,.2)}.hero-btn.outline{background:rgba(2,10,22,.7);color:#fff;border-color:#e4edf9}.hero-btn:hover{transform:translateY(-2px)}.about-pill{margin:18px auto 0;display:flex;gap:10px;align-items:center;justify-content:center;padding:11px 25px;border-radius:25px;background:rgba(2,8,18,.5);color:#fff;border:1px solid #91a8c9;cursor:pointer}.landing-features{display:grid;grid-template-columns:repeat(5,1fr);border-top:1px solid rgba(91,157,224,.22);background:#030914;padding:32px 5%;position:relative;z-index:2}.landing-features>div{text-align:center;padding:10px 22px;border-right:1px solid rgba(91,157,224,.18)}.landing-features>div:last-child{border:0}.landing-features span{font-size:32px;color:#f5b92e}.landing-features h3{margin:10px 0 7px;color:#fff}.landing-features p{margin:0;color:#aebbd0;font-size:13px;line-height:1.5}.landing-footer{height:100px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:#020711;border-top:1px solid rgba(245,185,46,.18);gap:5px}.landing-footer span{color:#f5b92e;font-weight:800;font-size:18px}.landing-footer small{color:#8e9db6}.inner-page-head,.auth-top{height:76px;padding:0 5%;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid rgba(91,157,224,.25);background:rgba(2,7,17,.85)}.back-icon{border:1px solid #49627e;background:#08182c;color:#fff;border-radius:10px;width:42px;height:42px;font-size:20px;cursor:pointer}.about-page{max-width:900px;margin:0 auto;padding:70px 20px;text-align:center}.about-logo{margin-bottom:25px}.about-logo .logo-crown{font-size:58px}.about-logo .logo-title{font-size:45px}.about-page h1{font-size:38px}.about-page h1 em{color:#f5b92e;font-style:normal}.about-page>p{color:#c3cfdf;font-size:18px;line-height:1.7}.about-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin:40px 0}.about-grid>div{background:rgba(8,24,44,.72);border:1px solid #1c6aa7;border-radius:16px;padding:25px;text-align:left}.about-grid b{color:#f5b92e}.about-grid p{color:#aebbd0;line-height:1.6}.hero-btn.small{min-width:210px;margin:auto}.auth-page{min-height:100vh;background:radial-gradient(circle at 50% 20%,rgba(8,90,174,.25),transparent 35%),#030916}.auth-card{width:min(470px,92vw);margin:50px auto;padding:34px;border:1px solid #1e69a5;border-radius:20px;background:rgba(5,17,32,.94);box-shadow:0 25px 80px rgba(0,0,0,.45)}.auth-mark{width:58px;height:58px;margin:auto;border-radius:50%;display:grid;place-items:center;background:#f5b92e;color:#10151d;font-size:30px}.auth-card h1{text-align:center;margin:18px 0 5px}.auth-card>p{text-align:center;color:#8fa0b8;margin-top:0}.auth-tabs{display:grid;grid-template-columns:1fr 1fr;gap:6px;background:#071225;border-radius:10px;padding:4px;margin:25px 0}.auth-tab{padding:11px;border:0;border-radius:8px;background:transparent;color:#9fb0c8;cursor:pointer;font-weight:800}.auth-tab.active{background:#123a61;color:#fff}.auth-card label{display:block;color:#cbd7e6;font-size:13px;margin:14px 0 7px}.auth-card input,.auth-card select{width:100%;padding:13px 14px;border-radius:9px;border:1px solid #294a6b;background:#07182d;color:#fff;outline:none}.auth-card input:focus,.auth-card select:focus{border-color:#f5b92e}.auth-options{display:flex;justify-content:space-between;align-items:center;margin:12px 0}.check{display:flex!important;align-items:center;gap:7px;font-size:12px!important;margin:0!important}.check input{width:auto}.link-btn{border:0;background:none;color:#f5bd37;cursor:pointer;padding:0}.auth-main-btn{width:100%;padding:14px;border:0;border-radius:25px;background:linear-gradient(180deg,#ffd24c,#e6a80c);font-weight:900;font-size:16px;cursor:pointer;margin-top:15px}.auth-or{display:flex;align-items:center;gap:12px;color:#6d7d92;margin:20px 0}.auth-or:before,.auth-or:after{content:"";height:1px;background:#24394f;flex:1}.google-btn{width:100%;padding:12px;border:1px solid #34506d;border-radius:24px;background:#0a1c31;color:#fff;font-weight:800;cursor:pointer}.switch-line{text-align:center!important;margin-top:20px!important;font-size:13px}.terms{margin:16px 0!important;line-height:1.4}.account-status{text-align:center}.account-user{text-align:center}.compact .language-button{height:40px}@media(max-width:900px){.landing-hero{grid-template-columns:1fr;padding:35px 6%;text-align:center}.hero-logo{order:0}.hero-copy{margin:auto}.hero-features{justify-content:center}.landing-features{grid-template-columns:repeat(2,1fr)}.landing-features>div{border-bottom:1px solid rgba(91,157,224,.18)}.landing-nav{display:none}.hero-copy h1{font-size:34px}.logo-title{font-size:42px}.about-grid{grid-template-columns:1fr}}@media(max-width:560px){.landing-header{padding:0 15px}.brand-mini{font-size:16px}.brand-crown{font-size:24px}.language-button{padding:0 10px}.hero-actions{justify-content:center}.hero-btn{width:100%}.landing-features{grid-template-columns:1fr}.landing-features>div{border-right:0}.auth-card{margin:25px auto;padding:23px}.auth-top{padding:0 15px}}


/* ===== DASHBOARD APRÈ CONNEXION ===== */
.dashboard-shell{min-height:100vh;background:radial-gradient(circle at 70% 15%,rgba(0,100,210,.20),transparent 30%),linear-gradient(135deg,#020711,#071426 58%,#020711);color:#fff;font-family:Inter,Segoe UI,Arial,sans-serif}
.dashboard-header{height:76px;border-bottom:1px solid rgba(212,175,55,.25);display:flex;align-items:center;gap:26px;padding:0 28px;background:rgba(2,7,17,.88);position:sticky;top:0;z-index:5;backdrop-filter:blur(10px)}
.dashboard-brand{font-size:20px;font-weight:800;white-space:nowrap}.dashboard-brand b{color:#f5bd32}.dashboard-crown{color:#f5bd32;font-size:30px;margin-right:8px}
.dashboard-nav{display:flex;align-items:center;gap:5px;flex:1;justify-content:center}.dash-nav{border:0;background:transparent;color:#dbe5f5;padding:19px 14px;cursor:pointer;font-weight:700;font-size:13px;border-bottom:2px solid transparent}.dash-nav:hover,.dash-nav.active{color:#f5bd32;border-bottom-color:#f5bd32}.dash-nav span{margin-left:4px}
.dashboard-user{display:flex;align-items:center;gap:9px;min-width:150px}.dash-avatar,.dash-big-avatar{display:grid;place-items:center;border-radius:50%;background:linear-gradient(145deg,#233a60,#0a1426);border:1px solid #d4af37;color:#f5bd32}.dash-avatar{width:38px;height:38px}.dashboard-user strong,.dashboard-user small{display:block}.dashboard-user small{font-size:10px;color:#7fd2ff;margin-top:2px}.dash-user-more{background:none;border:0;color:#fff;font-size:18px;cursor:pointer}
.dashboard-main{max-width:1180px;margin:0 auto;padding:30px 24px 28px}.welcome-card{min-height:190px;border:1px solid rgba(31,145,255,.35);border-radius:18px;overflow:hidden;display:flex;align-items:center;justify-content:space-between;padding:30px 42px;background:radial-gradient(circle at 85% 50%,rgba(0,112,255,.30),transparent 35%),linear-gradient(110deg,#07111f,#0a1d35);box-shadow:0 15px 45px rgba(0,0,0,.25)}.welcome-kicker{font-size:12px;letter-spacing:3px;color:#83bfff;font-weight:800}.welcome-copy h1{font-size:35px;margin:8px 0 2px}.welcome-copy h1 span{color:#f5bd32}.welcome-copy p{margin:0;color:#c8d4e8;font-size:18px}.welcome-copy>strong{font-size:14px}.welcome-line{width:180px;height:2px;background:linear-gradient(90deg,#f5bd32,transparent);margin:18px 0}.welcome-world{font-size:110px;opacity:.9;filter:drop-shadow(0 0 20px rgba(0,130,255,.35))}
.dashboard-balance-row{display:grid;grid-template-columns:1fr 1fr 1.25fr;gap:14px;margin:18px 0}.dash-balance-card,.dash-profile-card{background:#081322;border:1px solid #12385f;border-radius:14px;padding:16px 18px;position:relative}.dash-balance-card small,.dash-profile-card small{display:block;color:#8da1bc;font-size:12px}.dash-balance-card strong{display:block;font-size:25px;color:#f5bd32;margin-top:5px}.dash-balance-card button{position:absolute;right:15px;top:25px;width:28px;height:28px;border-radius:50%;border:1px solid #1b9cff;background:#062442;color:#7dc9ff;cursor:pointer}.dash-profile-card{display:flex;align-items:center;gap:14px}.dash-profile-card strong{display:block;font-size:16px}.dash-big-avatar{width:55px;height:55px;font-size:24px}
.dashboard-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.dashboard-card{min-height:155px;text-align:left;border:1px solid #0f4a7d;border-radius:15px;background:linear-gradient(145deg,#081727,#06101d);color:#fff;padding:20px;cursor:pointer;transition:.18s;display:flex;flex-direction:column;align-items:flex-start}.dashboard-card:hover{transform:translateY(-3px);border-color:#f5bd32;box-shadow:0 10px 28px rgba(0,0,0,.25)}.dashboard-card.gold-card{border-color:#9d7820;background:linear-gradient(145deg,#111a22,#1a160b)}.dash-card-icon{width:45px;height:45px;border-radius:50%;display:grid;place-items:center;background:#061d33;border:1px solid #f5bd32;font-size:22px;margin-bottom:13px}.dashboard-card strong{font-size:18px;margin-bottom:7px}.dashboard-card small{color:#91a5c1;line-height:1.35}.dashboard-footer-banner{margin-top:18px;padding:14px 18px;border-radius:12px;border:1px solid rgba(212,175,55,.35);background:linear-gradient(90deg,#0a1422,#111b28,#0a1422);display:flex;align-items:center;gap:12px}.dashboard-footer-banner span{font-size:25px;color:#f5bd32}.dashboard-footer-banner strong{flex:1;color:#f5bd32}.dashboard-footer-banner button{border:1px solid #7f1d1d;background:#4a1010;color:#fff;border-radius:8px;padding:8px 13px;font-weight:700;cursor:pointer}
@media(max-width:900px){.dashboard-header{padding:0 15px;gap:10px}.dashboard-nav{gap:0}.dash-nav{padding:18px 7px;font-size:11px}.dashboard-user{min-width:auto}.dashboard-user>div:nth-child(2){display:none}.dashboard-grid{grid-template-columns:repeat(2,1fr)}.dashboard-balance-row{grid-template-columns:1fr}.welcome-card{padding:25px}.welcome-world{font-size:75px}}
@media(max-width:600px){.dashboard-brand{font-size:15px}.dashboard-crown{font-size:23px}.dash-nav span{display:none}.dashboard-main{padding:18px 12px}.welcome-card{min-height:175px;padding:22px}.welcome-copy h1{font-size:27px}.welcome-world{font-size:55px}.dashboard-grid{gap:9px}.dashboard-card{min-height:145px;padding:14px}.dashboard-card strong{font-size:15px}.dashboard-footer-banner{align-items:flex-start;flex-wrap:wrap}.dashboard-footer-banner strong{min-width:70%}}


/* ===== NOUVELLE IDENTITE VISUELLE : MR_JERY MORPION ===== */
:root{--neo-bg:#080b16;--neo-panel:#11182a;--neo-panel2:#171f35;--neo-border:#293650;--neo-text:#f5f7ff;--neo-muted:#a7b3cc;--neo-cyan:#43e0d0;--neo-purple:#8b70ff;--neo-blue:#438cff}
body{background:radial-gradient(ellipse at 50% -10%,rgba(83,88,255,.18),transparent 45%),#080b16!important;color:var(--neo-text)!important;font-family:Inter,"Segoe UI",Arial,sans-serif!important}
#onlineScreen,#spectatorScreen,#waitingRoomScreen{max-width:1120px;margin:0 auto;padding:30px 22px 40px;min-height:calc(100vh - 30px);position:relative}
#onlineScreen h1,#spectatorScreen h1,#waitingRoomScreen h1{font-size:clamp(28px,4vw,42px);font-weight:900;letter-spacing:-1.2px;margin:16px 0 10px;background:linear-gradient(100deg,#fff 15%,#b4b9ff 55%,#43e0d0);-webkit-background-clip:text;background-clip:text;color:transparent}
#onlineScreen h1:after,#spectatorScreen h1:after,#waitingRoomScreen h1:after{content:"";display:block;width:74px;height:4px;border-radius:8px;background:linear-gradient(90deg,var(--neo-purple),var(--neo-cyan));margin:14px auto 0}
#onlineScreen:before,#spectatorScreen:before,#waitingRoomScreen:before{content:"MR_JERY  /  ARENA";display:block;text-align:left;color:#7e8da9;font-size:11px;font-weight:900;letter-spacing:3px;padding:6px 0 18px;border-bottom:1px solid rgba(130,153,200,.15)}
#onlineScreen .online-box{max-width:900px;margin:30px auto 22px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
#onlineScreen .online-choice{position:relative;min-height:145px;padding:26px 22px 24px;border:1px solid var(--neo-border);border-radius:20px;background:linear-gradient(145deg,rgba(25,35,59,.98),rgba(14,20,37,.98));color:#f7f8ff;font-size:19px;font-weight:800;text-align:left;box-shadow:0 12px 28px rgba(0,0,0,.18);transition:transform .18s,border-color .18s,background .18s;overflow:hidden}
#onlineScreen .online-choice:before{content:"";position:absolute;inset:0 auto 0 0;width:4px;background:linear-gradient(var(--neo-purple),var(--neo-cyan));opacity:.85}
#onlineScreen .online-choice:after{content:"↗";position:absolute;right:20px;top:18px;width:34px;height:34px;border-radius:11px;display:grid;place-items:center;background:rgba(129,112,255,.13);border:1px solid rgba(139,112,255,.3);color:#a99aff;font-size:18px}
#onlineScreen .online-choice:hover{transform:translateY(-4px);border-color:var(--neo-purple);background:linear-gradient(145deg,#202c4c,#121a30)}
#onlineScreen .online-choice:focus-visible,#spectatorScreen button:focus-visible{outline:3px solid var(--neo-cyan);outline-offset:3px}
#onlineScreen .online-choice:nth-child(1){background:radial-gradient(circle at 100% 0,rgba(67,140,255,.19),transparent 45%),linear-gradient(145deg,#192742,#101729)}
#onlineScreen .online-choice:nth-child(2){background:radial-gradient(circle at 100% 0,rgba(67,224,208,.14),transparent 45%),linear-gradient(145deg,#192b3a,#101729)}
#onlineScreen .online-choice:nth-child(3){background:radial-gradient(circle at 100% 0,rgba(139,112,255,.16),transparent 45%),linear-gradient(145deg,#242341,#101729)}
#onlineScreen .online-choice:nth-child(4){background:radial-gradient(circle at 100% 0,rgba(255,184,91,.13),transparent 45%),linear-gradient(145deg,#30283c,#101729)}
#onlineScreen .friend-box,#onlineScreen .searching-box,#onlineScreen .online-players-box,#onlineScreen .game-invite-box,#onlineScreen .room{max-width:900px;border:1px solid var(--neo-border);border-radius:18px;background:linear-gradient(145deg,rgba(20,29,49,.98),rgba(12,17,31,.98));box-shadow:0 14px 34px rgba(0,0,0,.18);color:var(--neo-text)}
#onlineScreen .friend-box{padding:22px;gap:12px}
#onlineScreen .friend-box input,#spectatorScreen input{background:#090f1f!important;color:#fff!important;border:1px solid #35435f!important;border-radius:12px!important;padding:15px!important;letter-spacing:2px}
#onlineScreen .friend-box button,#onlineScreen .searching-box button,#onlineScreen .game-invite-actions button,#spectatorScreen button{border:1px solid rgba(139,112,255,.45);border-radius:11px;background:linear-gradient(120deg,#6d5be7,#398edb);color:white;font-weight:800;padding:12px 18px;cursor:pointer;transition:transform .18s,filter .18s}
#onlineScreen .friend-box button:hover,#onlineScreen .searching-box button:hover,#spectatorScreen button:hover{filter:brightness(1.12);transform:translateY(-1px)}
#onlineScreen .online-players-box{padding:20px;text-align:left}
#onlineScreen .online-players-title{color:var(--neo-cyan);text-align:left;font-size:15px;letter-spacing:.5px}
#onlineScreen .online-player-row{background:#0a1020;border:1px solid #26334d;border-radius:12px;padding:13px}
#onlineScreen .online-player-invite{background:#192642;color:#fff;border-color:#4a5c80}
#onlineScreen .room{padding:18px;margin:18px auto;color:var(--neo-muted)}
#onlineScreen .room span{color:var(--neo-cyan);font-weight:900;letter-spacing:2px}
#onlineScreen .back-button,#spectatorScreen .back-button,#waitingRoomScreen .back-button{border:1px solid #33415d;border-radius:12px;background:#141d31;color:#dce5fa;padding:12px 22px;font-weight:800;cursor:pointer}
#onlineScreen .back-button:hover,#spectatorScreen .back-button:hover,#waitingRoomScreen .back-button:hover{border-color:var(--neo-cyan);color:var(--neo-cyan)}
#onlineScreen .error,#spectatorScreen .error{color:#ff8c9a}
#spectatorScreen .spectator-box,#waitingRoomScreen .waiting-box{max-width:900px;margin:28px auto;padding:25px;border:1px solid var(--neo-border);border-radius:20px;background:linear-gradient(145deg,rgba(20,29,49,.98),rgba(12,17,31,.98));box-shadow:0 18px 45px rgba(0,0,0,.22);text-align:left}
#spectatorScreen .spectator-box .status{font-size:17px;font-weight:800;color:#e9edff;margin-bottom:18px}
#spectatorScreen .live-match-list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:13px;margin:16px 0}
#spectatorScreen .live-match-list:empty:before{content:"Pa gen match ki parèt isit la pou kounye a. Peze Actualiser pou tcheke ankò.";display:block;grid-column:1/-1;border:1px dashed #35415b;border-radius:14px;padding:24px;text-align:center;color:var(--neo-muted);line-height:1.6}
#spectatorScreen .live-match-list>div,#spectatorScreen .live-match-list>button{min-width:0;border-radius:14px!important;background:#0c1427!important;border:1px solid #2a3855!important;color:#f6f7ff!important;padding:17px!important}
#spectatorScreen #refreshSpectatorBtn{margin-top:12px}
#waitingRoomScreen .waiting-list{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:20px 0}
#waitingRoomScreen .waiting-player{background:#0b1222;border:1px solid #293651;border-radius:12px;padding:16px;color:#dce5fa}
#waitingRoomScreen .waiting-status,#waitingRoomScreen .status{color:var(--neo-cyan)}
@media(max-width:650px){#onlineScreen,#spectatorScreen,#waitingRoomScreen{padding:18px 12px 30px}#onlineScreen .online-box{grid-template-columns:1fr;gap:12px;margin-top:22px}#onlineScreen .online-choice{min-height:105px;padding:22px 18px;font-size:17px}#spectatorScreen .live-match-list,#waitingRoomScreen .waiting-list{grid-template-columns:1fr}#spectatorScreen .spectator-box,#waitingRoomScreen .waiting-box{padding:16px}}


/* Paramètres d'invitation et styles locaux du tableau */
.invite-settings-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;text-align:left;margin:10px 0}
.invite-settings-grid label,.board-style-label{display:flex;flex-direction:column;gap:6px;color:#E5E7EB;font-size:14px;font-weight:700}
.invite-settings-grid select,.board-style-label select{width:100%;min-height:44px;padding:9px 10px;border-radius:9px;border:1px solid #4B5563;background:#111827;color:#fff;font-size:15px}
.board-style-label{max-width:100%;text-align:left}
.board-style-midnight .board{background:#172033!important;border-color:#64748b!important}
.board-style-midnight .cell{border-color:#64748b!important}
.board-style-mint .board{background:#d9fbe8!important;border-color:#4d8d70!important}
.board-style-mint .cell{border-color:#8bbda1!important}
.board-style-rose .board{background:#fff0f5!important;border-color:#d68aa8!important}
.board-style-rose .cell{border-color:#e3a9be!important}
.board-style-sand .board{background:#f4e7c5!important;border-color:#c5a96b!important}
.board-style-sand .cell{border-color:#cbb783!important}
@media(max-width:480px){.invite-settings-grid{grid-template-columns:1fr}}

/* Keep the original landing page visible so players can choose Connexion or Créer un compte. */

/* Ajustements responsive MR_Jery : tableaux et navigation */
html { -webkit-text-size-adjust: 100%; }
.dashboard-shell, .dashboard-main, .dashboard-header, .dashboard-nav,
.wallet-box, .bet-box, .admin-box, .profile-box { min-width: 0; max-width: 100%; box-sizing: border-box; }
.dashboard-header { flex-wrap: wrap; }
.dashboard-nav { flex-wrap: wrap; min-width: 0; }
.dash-nav { white-space: nowrap; }
.wallet-grid { grid-template-columns: repeat(auto-fit, minmax(min(100%, 170px), 1fr)); }
.history-item, .profile-value, .online-player-row, .status, .notice-test { overflow-wrap: anywhere; }
/* Nenpòt tablo HTML dwe rete andedan ekran an sou telefòn. */
table { width: 100%; max-width: 100%; border-collapse: collapse; }
.table-wrap, .table-responsive, .ranking-table-wrap { width: 100%; max-width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; }
td, th { overflow-wrap: anywhere; }
@media (max-width: 600px) {
  .dashboard-header { align-items: flex-start; }
  .dashboard-brand { flex: 1 1 100%; }
  .dashboard-nav { order: 3; width: 100%; justify-content: flex-start; overflow-x: auto; flex-wrap: nowrap; }
  .dash-nav { padding: 10px 8px; font-size: 11px; }
  .dashboard-user { margin-left: auto; }
  .wallet-box, .bet-box, .admin-box { padding: 12px; }
  .board-area { margin-left: auto; margin-right: auto; }
}
</style>
<style>
.match-communication{max-width:850px;margin:18px auto;padding:16px;border:1px solid #33415d;border-radius:16px;background:#10192b;color:#edf2ff;text-align:left;box-shadow:0 12px 30px rgba(0,0,0,.18)}
.match-comm-header{display:flex;align-items:center;justify-content:space-between;gap:10px}.match-comm-header h3{margin:0;font-size:18px}.match-comm-toggle,.match-chat-form button,.match-voice-controls button{border:0;border-radius:10px;padding:10px 14px;background:#5145cd;color:white;font-weight:800;cursor:pointer}
.match-chat-messages{height:190px;overflow-y:auto;padding:10px;margin:12px 0;background:#080f1e;border:1px solid #2b3852;border-radius:12px;display:flex;flex-direction:column;gap:8px}.match-chat-message{padding:8px 10px;border-radius:10px;background:#1a2941;overflow-wrap:anywhere}.match-chat-message strong{color:#8dd9ff}.match-chat-message small{opacity:.65;margin-left:8px}.match-chat-form{display:flex;gap:8px}.match-chat-form input{flex:1;min-width:0;border-radius:10px;border:1px solid #35435f;background:#080f1e;color:white;padding:12px}.match-voice-controls{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-top:12px}.match-comm-note{font-size:12px;opacity:.72;margin-top:9px}.match-communication audio{display:none}
@media(max-width:600px){.match-communication{margin:12px 8px;padding:12px}.match-chat-messages{height:150px}}

/* JERY GAMES - menu addition only; existing game screens remain unchanged */
.jery-games-head{display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap;margin:22px 0}
.jery-games-head h1{margin:0;color:#f5b92e}.jery-games-head p{color:#aebbd0;margin:7px 0 0}
.jery-games-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(205px,1fr));gap:14px;margin:20px 0 32px}
.jery-game-card{position:relative;display:flex;flex-direction:column;align-items:flex-start;gap:9px;min-height:155px;padding:18px;border-radius:16px;border:1px solid #254766;background:linear-gradient(145deg,#0b1c31,#07101f);color:#fff;text-align:left;cursor:pointer;transition:transform .15s,border-color .15s}
.jery-game-card:hover{transform:translateY(-2px);border-color:#f5b92e}.jery-game-card .jery-game-icon{font-size:30px}.jery-game-card strong{font-size:16px}.jery-game-card small{color:#aebbd0;line-height:1.4}.jery-game-status{margin-top:auto;font-size:11px;font-weight:900;letter-spacing:.04em;color:#f5c13a;border:1px solid #715719;border-radius:20px;padding:5px 9px}
.jery-game-card.available{border-color:#267c5b}.jery-game-card.available .jery-game-status{color:#75e5ad;border-color:#267c5b}
.jery-games-note{padding:14px 16px;border-radius:12px;background:#0a1a2c;border:1px solid #254766;color:#c5d3e5;line-height:1.5}
</style>

<style id="mrjery-rank-styles">
.rank-pill{display:inline-flex;align-items:center;gap:7px;border:1px solid currentColor;border-radius:999px;padding:5px 10px;font-weight:900;font-size:12px;white-space:nowrap;background:rgba(255,255,255,.05)}
.rank-panel{max-width:1000px;margin:24px auto;padding:20px;background:#081322;border:1px solid #234766;border-radius:16px;color:#edf5ff}
.rank-current{display:grid;grid-template-columns:84px minmax(0,1fr);gap:16px;align-items:center;padding:18px;border-radius:14px;background:linear-gradient(120deg,#0c2540,#101a2c);border:1px solid #315574}
.rank-emblem{width:76px;height:76px;border-radius:50%;display:grid;place-items:center;font-size:32px;font-weight:1000;background:#101c2d;border:3px solid currentColor}
.rank-progress{height:12px;background:#25364b;border-radius:20px;overflow:hidden;margin:10px 0}.rank-progress>span{display:block;height:100%;width:0;background:linear-gradient(90deg,#1c9cff,#f5bd32);transition:width .25s}
.rank-table{width:100%;border-collapse:collapse;margin-top:18px}.rank-table th,.rank-table td{text-align:left;padding:10px;border-bottom:1px solid #26384b}.rank-table th{color:#f5bd32}.rank-table tr.current-rank{background:#17314a}.rank-small{color:#9fb1c7;font-size:13px}.rank-actions{display:flex;gap:10px;flex-wrap:wrap;margin:15px 0}.rank-actions button{padding:10px 14px;border-radius:9px;border:1px solid #34536e;background:#0b2138;color:white;font-weight:800;cursor:pointer}
@media(max-width:600px){.rank-panel{padding:12px}.rank-table th,.rank-table td{padding:8px 5px;font-size:12px}.rank-current{grid-template-columns:60px minmax(0,1fr)}.rank-emblem{width:56px;height:56px;font-size:24px}}
</style>

</head>

<body>

<div class="app">

<!-- MENU PRINCIPAL -->

<section id="landingScreen" class="screen active">

    <div class="landing-shell">
        <header class="landing-header">
            <div class="brand-mini" aria-label="MR Jery Morpion"><span class="brand-crown">♛</span><span>MR_Jery <b>Morpion</b></span></div>
            <nav class="landing-nav">
                <button type="button" class="nav-link active" id="landingHomeBtn">⌂ <span data-i18n="navHome">Accueil</span></button>
                <button type="button" class="nav-link" id="landingGameBtn">🎮 <span data-i18n="navGame">Jeu</span></button>
                <button type="button" class="nav-link" id="landingAboutBtn">ⓘ <span data-i18n="navAbout">À propos</span></button>
            </nav>
            <div class="language-wrap">
                <button type="button" class="language-button" id="languageButton">🌐 <span id="currentLanguage">Français</span> <span>⌄</span></button>
                <div class="language-menu" id="languageMenu">
                    <button data-lang="fr">🇫🇷 Français</button>
                    <button data-lang="en">🇺🇸 English</button>
                    <button data-lang="ht">🇭🇹 Kreyòl Ayisyen</button>
                </div>
            </div>
        </header>

        <main class="landing-hero">
            <div class="world-map" aria-hidden="true"></div>
            <div class="hero-logo">
                <div class="logo-crown">♛</div>
                <div class="logo-ring">
                    <div class="logo-board-mini"><i></i><i></i><i></i><i></i><i></i><i></i></div>
                </div>
                <div class="logo-title"><span>MR_Jery</span><strong>MORPION</strong></div>
            </div>
            <div class="hero-copy">
                <h1 data-i18n="heroTitle">Plis pase yon jwèt... <em>yon kominote!</em></h1>
                <p data-i18n="heroText">Jwe ak moun ki soti nan tout mond lan, leve defi, fè konpetisyon epi monte nan klasman MR_Jery Morpion.</p>
                <div class="hero-features">
                    <span>🌍 <b data-i18n="fGlobal">Jwè nan tout mond lan</b></span>
                    <span>🛡️ <b data-i18n="fSecure">Sekirize &amp; serye</b></span>
                    <span>⚡ <b data-i18n="fFast">Rapid &amp; fluid</b></span>
                    <span>♛ <b data-i18n="fRewards">Defi &amp; rekonpans</b></span>
                </div>
                <div class="hero-actions">
                    <button class="hero-btn gold" id="landingLoginBtn">👤 <span data-i18n="login">Connexion</span> <b>›</b></button>
                    <button class="hero-btn outline" id="landingRegisterBtn">👥 <span data-i18n="register">Créer un compte</span> <b>›</b></button>
                </div>
                <button class="about-pill" id="landingAboutPill">ⓘ <span data-i18n="about">À propos</span> <b>›</b></button>
            </div>
        </main>

        <section class="landing-features">
            <div><span>🌐</span><h3 data-i18n="cardOnline">Jwe Anliy</h3><p data-i18n="cardOnlineText">Defi e jwè nan tout peyi.</p></div>
            <div><span>🛡️</span><h3 data-i18n="cardSecurity">Sekirite</h3><p data-i18n="cardSecurityText">Pwoteksyon pou kont ou ak jwèt yo.</p></div>
            <div><span>👥</span><h3 data-i18n="cardCommunity">Kominote</h3><p data-i18n="cardCommunityText">Rankontre jwè ak nouvo advèsè.</p></div>
            <div><span>⚡</span><h3 data-i18n="cardFast">Rapid</h3><p data-i18n="cardFastText">Match vit, san konplikasyon.</p></div>
            <div><span>🏆</span><h3 data-i18n="cardChallenge">Defi</h3><p data-i18n="cardChallengeText">Montre kapasite w sou tablo a.</p></div>
        </section>

        <footer class="landing-footer"><span>MR_Jery Morpion</span><small data-i18n="footer">Jwe • Defi • Gagne</small></footer>
    </div>

</section>

<section id="homeScreen" class="screen">

    <h1>MR JERY MOPION</h1>

    <div class="main-menu">

        <button class="menu-button" id="robotMode">
            🤖 Jouer avec Robot
        </button>

        <button class="menu-button" id="localMode">
            👥 2 Utilisateurs
        </button>

        <button class="menu-button" id="onlineMode">
            🌐 Jouer en Ligne
        </button>

        <button class="menu-button" id="accountMode">
            👤 Compte joueur
        </button>

    </div>

</section>


<!-- À PROPOS -->
<section id="aboutScreen" class="screen">
    <div class="inner-page-head">
        <button class="back-icon" id="aboutBack">←</button>
        <div class="brand-mini"><span class="brand-crown">♛</span><span>MR_Jery <b>Morpion</b></span></div>
        <div class="language-wrap compact"><button type="button" class="language-button" id="aboutLanguageButton">🌐 <span id="aboutCurrentLanguage">Français</span> ⌄</button></div>
    </div>
    <div class="about-page">
        <div class="about-logo"><div class="logo-crown">♛</div><div class="logo-title"><span>MR_Jery</span><strong>MORPION</strong></div></div>
        <h1 data-i18n="aboutTitle">Plis pase yon jwèt... <em>yon kominote!</em></h1>
        <p data-i18n="aboutText">MR_Jery Morpion se yon platfòm pou jwe, rankontre jwè, leve defi epi suiv pwogrè ou.</p>
        <div class="about-grid">
            <div><b>🎯 <span data-i18n="vision">Vizyon</span></b><p data-i18n="visionText">Rasanble jwè morpion atravè mond lan.</p></div>
            <div><b>🚀 <span data-i18n="mission">Misyon</span></b><p data-i18n="missionText">Bay yon eksperyans rapid, senp ak agreyab.</p></div>
            <div><b>🤝 <span data-i18n="values">Valè</span></b><p data-i18n="valuesText">Respè, fair-play, kominote ak evolisyon.</p></div>
        </div>
        <button class="hero-btn gold small" id="aboutJoinBtn">👥 <span data-i18n="register">Créer un compte</span> ›</button>
    </div>
</section>

<!-- COMPTE -->
<section id="accountScreen" class="screen">
    <div class="auth-page">
        <div class="auth-top"><button class="back-icon" id="accountBack">←</button><div class="brand-mini"><span class="brand-crown">♛</span><span>MR_Jery <b>Morpion</b></span></div><div></div></div>
        <div class="auth-card">
            <div class="auth-mark">♛</div>
            <h1 id="authTitle">Connexion</h1>
            <p id="authSubtitle">Connecte-toi à ton compte</p>
            <div class="auth-tabs">
                <button id="authLoginTab" class="auth-tab active">Connexion</button>
                <button id="authRegisterTab" class="auth-tab">Créer un compte</button>
            </div>

            <div id="loginPanel">
                <label>Nom d'utilisateur ou e-mail</label>
                <input id="loginInput" type="text" placeholder="Nom d'utilisateur ou e-mail">
                <label>Mot de passe</label>
                <input id="loginPassword" type="password" placeholder="Mot de passe">
                <div class="auth-options"><label class="check"><input type="checkbox"> <span>Se souvenir de moi</span></label><button type="button" class="link-btn">Mot de passe oublié ?</button></div>
                <button class="auth-main-btn" id="loginBtn" type="button">Se connecter <b>›</b></button>
                <div class="auth-or"><span>OU</span></div>
                <button class="google-btn" type="button">G <span>Se connecter avec Google</span></button>
                <p class="switch-line">Vous n'avez pas de compte ? <button type="button" id="goRegisterBtn" class="link-btn">Créer un compte</button></p>
            </div>

            <div id="registerPanel" style="display:none">
                <label>Nom d'utilisateur</label>
                <input id="registerUsername" type="text" maxlength="50" placeholder="Nom d'utilisateur">
                <label>E-mail</label>
                <input id="registerEmail" type="email" maxlength="255" placeholder="E-mail">
                <label>Mot de passe</label>
                <input id="registerPassword" type="password" placeholder="Mot de passe">
                <label>Confirmer le mot de passe</label>
                <input id="registerPasswordConfirmation" type="password" placeholder="Confirmer le mot de passe">
                <label>Pays de résidence</label>
                <select id="registerCountry"><option>Haiti</option><option>United States</option><option>Canada</option><option>France</option><option>Dominican Republic</option><option>Other</option></select>
                <label>Langue préférée</label>
                <select id="registerLanguage"><option value="fr">Français</option><option value="en">English</option><option value="es">Español</option><option value="ht">Kreyòl Ayisyen</option><option value="pt">Português</option></select>
                <label class="check terms"><input type="checkbox" id="registerTerms"> <span>J'accepte les conditions d'utilisation et la politique de confidentialité.</span></label>
                <button class="auth-main-btn" id="registerBtn" type="button">Créer mon compte <b>›</b></button>
                <p class="switch-line">Vous avez déjà un compte ? <button type="button" id="goLoginBtn" class="link-btn">Se connecter</button></p>
            </div>
            <div id="accountStatus" class="account-status"></div>
            <div id="accountUser" class="account-user"></div>
        </div>
    </div>
</section>

<!-- MENU APRÈS CONNEXION -->
<section id="accountMenuScreen" class="screen">
  <div class="dashboard-shell">
    <header class="dashboard-header">
      <div class="dashboard-brand"><span class="dashboard-crown">♛</span><span>MR_Jery <b>Morpion</b></span></div>
      <nav class="dashboard-nav">
        <button type="button" class="dash-nav active" id="accountPlayBtn">⌂ <span>Accueil</span></button>
        <button type="button" class="dash-nav" id="accountOnlineBtn">🎮 <span>Jeu</span></button>
        <button type="button" class="dash-nav" id="dashboardRankingBtn">🏆 <span>Classement</span></button>
        <button type="button" class="dash-nav" id="dashboardPlayersBtn">👥 <span>Jwè & Nivo</span></button>
        <button type="button" class="dash-nav" id="profileBtn">ⓘ <span>Profil</span></button>
        <button type="button" class="dash-nav" id="walletTopBtn">💰 <span>Wallet</span></button>
        <button type="button" class="dash-nav" id="adminTopBtn">👑 <span>Admin</span></button>
      </nav>
      <div class="dashboard-user">
        <div class="dash-avatar">♟</div>
        <div><strong id="dashboardUsername">Joueur</strong><small id="dashboardLevel">Niveau 1</small></div>
        <button type="button" id="dashboardUserMenu" class="dash-user-more">⌄</button>
      </div>
    </header>

    <main class="dashboard-main">
      <section class="welcome-card">
        <div class="welcome-copy">
          <div class="welcome-kicker">BIENVENUE SUR</div>
          <h1>MR_Jery <span>Morpion</span></h1>
          <p>Joue • Défi • Gagne</p>
          <div class="welcome-line"></div>
          <strong>Prêt pour ton prochain match ?</strong>
        </div>
        <div class="welcome-world">🌍</div>
      </section>

      <section class="dashboard-balance-row">
        <div class="dash-balance-card"><small>Solde USD</small><strong id="dashboardUsd">$0.00</strong><button type="button" id="dashboardDepositUsd">＋</button></div>
        <div class="dash-balance-card"><small>Solde HTG</small><strong id="dashboardHtg">0 HTG</strong><button type="button" id="dashboardDepositHtg">＋</button></div>
        <div class="dash-profile-card"><div class="dash-big-avatar">♟</div><div><strong id="accountMenuUser">👤 Connecté</strong><small>Joueur MR_Jery</small></div></div>
      </section>

      <section class="dashboard-grid">
        <button class="dashboard-card" id="dashboardOnlineCard"><span class="dash-card-icon">👥</span><strong>Jwe Anliy</strong><small>Affronte des joueurs du monde entier.</small></button>
        <button class="dashboard-card" id="dashboardFriendCard"><span class="dash-card-icon">🤝</span><strong>Jwe ak yon zanmi</strong><small>Envite yon zanmi epi jwe ansanm.</small></button>
        <button class="dashboard-card" id="dashboardChallengeCard"><span class="dash-card-icon">🛡️</span><strong>Defi</strong><small>Kreye oswa aksepte defi.</small></button>
        <button class="dashboard-card gold-card" id="dashboardBetCard"><span class="dash-card-icon">💰</span><strong>Paryaj</strong><small>Mise, jwe epi suiv rekonpans yo.</small></button>
        <button class="dashboard-card" id="dashboardSpectatorCard"><span class="dash-card-icon">👁️</span><strong>Spectateur</strong><small>Gade match yo an dirèk.</small></button>
        <button class="dashboard-card" id="dashboardRobotCard"><span class="dash-card-icon">🤖</span><strong>Robot</strong><small>Jwe kont IA a pou antrene.</small></button>
        <button class="dashboard-card" id="dashboardRankingCard"><span class="dash-card-icon">🏆</span><strong>Classement</strong><small>Gade pi bon jwè yo.</small></button>
        <button class="dashboard-card" id="dashboardPlayersCard"><span class="dash-card-icon">👥🏆</span><strong>Tout jwè & nivo yo</strong><small>Gade tout kont ki enskri yo, menm jwè offline, sig yo ak 30 nivo MR_Jery yo.</small></button>
        <button class="dashboard-card gold-card" id="dashboardGamesCard"><span class="dash-card-icon">🎮</span><strong>JERY GAMES</strong><small>Tout jwèt platfòm nan nan yon sèl meni.</small></button>
        <button class="dashboard-card" id="walletBtn"><span class="dash-card-icon">👛</span><strong>Wallet</strong><small>Jere balans ak tranzaksyon ou yo.</small></button>
      </section>

      <section class="dashboard-footer-banner"><span>♛</span><strong>Rantre nan kominote a epi vin yon lejand!</strong><button type="button" id="logoutBtn">🚪 Déconnexion</button></section>
    </main>
  </div>
</section>

<!-- JERY GAMES: menu added without replacing existing screens -->
<section id="jeryGamesScreen" class="screen">
  <div class="inner-page-head">
    <button type="button" class="back-icon" id="jeryGamesBack" aria-label="Retour">←</button>
    <div class="brand-mini"><span class="brand-crown">♛</span> MR_<b>Jery</b> GAMES</div>
    <span></span>
  </div>
  <main style="max-width:1200px;margin:0 auto;padding:24px 18px 45px">
    <div class="jery-games-head"><div><h1>🎮 JERY GAMES</h1><p>Yon sèl kont, plizyè jwèt. Chwazi jwèt ou vle jwe.</p></div></div>
    <div class="jery-games-note">✅ <strong>MR_Jery Morpion</strong> rete jwèt ki disponib la. Lòt jwèt yo make <strong>Bientôt disponible</strong> jiskaske yo devlope epi teste. Sa pa chanje jwèt, kont, wallet oswa sistèm match ki te deja la.</div>
    <div class="jery-games-grid" id="jeryGamesGrid">
      <button class="jery-game-card available" data-game="morpion"><span class="jery-game-icon">⚫🔴</span><strong>MR_Jery Morpion</strong><small>Jwe anliy, ak zanmi oswa kont robot.</small><span class="jery-game-status">DISPONIB</span></button>
      <button class="jery-game-card" data-game="domino"><span class="jery-game-icon">🁢</span><strong>Domino Jery</strong><small>2–4 jwè • estrateji</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="ludo"><span class="jery-game-icon">🎲</span><strong>Ludo Jery</strong><small>2–4 jwè • jwèt fanmi</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="chess"><span class="jery-game-icon">♟️</span><strong>Echek Jery</strong><small>Estrateji ak refleksyon</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="checkers"><span class="jery-game-icon">🔴⚫</span><strong>Dam Jery</strong><small>Defi 1 kont 1</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="connect4"><span class="jery-game-icon">🟡🔴</span><strong>Puissance 4 Jery</strong><small>Aliyen 4 pyès</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="tictactoe"><span class="jery-game-icon">❌⭕</span><strong>Morpion 3×3</strong><small>Match rapid</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="battleship"><span class="jery-game-icon">⚓</span><strong>Bataille Navale</strong><small>Jwenn bato advèsè a</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="reversi"><span class="jery-game-icon">⚫⚪</span><strong>Reversi / Othello</strong><small>Kontwole tablo a</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="backgammon"><span class="jery-game-icon">🎲</span><strong>Backgammon</strong><small>Deplase pyès ak zo</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="chinese-checkers"><span class="jery-game-icon">⭐</span><strong>Dames Chinoises</strong><small>Jiska 6 jwè, selon règ jwèt la</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="mills"><span class="jery-game-icon">⚙️</span><strong>Moulin</strong><small>Fòme liy 3 pyès</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="awale"><span class="jery-game-icon">🪵</span><strong>Awalé / Mancala</strong><small>Kolekte grenn ak estrateji</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="rps"><span class="jery-game-icon">✊📄✂️</span><strong>Wòch, Papye, Sizo</strong><small>Defi rapid</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="words"><span class="jery-game-icon">🔤</span><strong>Jery Mots</strong><small>Devine mo an Kreyòl, Franse oswa Anglè</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="hangman"><span class="jery-game-icon">🪢</span><strong>Jeu du Pendu</strong><small>Devine mo kache a</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="memory"><span class="jery-game-icon">🧠</span><strong>Memory Jery</strong><small>Jwenn pè kat yo</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="minesweeper"><span class="jery-game-icon">💣</span><strong>Démineur</strong><small>Jwenn kare ki an sekirite yo</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="number"><span class="jery-game-icon">🔢</span><strong>Jery Number Challenge</strong><small>Devinèt nimewo ak tan limite</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="cards"><span class="jery-game-icon">🃏</span><strong>Bataille de Cartes</strong><small>Jwèt kat ak règ defini</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="puzzle"><span class="jery-game-icon">🧩</span><strong>Jery Puzzle Battle</strong><small>Rezoud devinèt anvan advèsè a</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
      <button class="jery-game-card" data-game="quiz"><span class="jery-game-icon">🏆</span><strong>Jery Quiz Battle</strong><small>Kilti jeneral, syans, istwa ak espò</small><span class="jery-game-status">BIENTÔT DISPONIBLE</span></button>
    </div>
  </main>
</section>

<!-- PROFIL -->
<section id="profileScreen" class="screen">
    <h1>👤 Mon profil</h1>
    <div class="profile-box">
        <div class="profile-row"><span class="profile-label">Pseudo</span><span id="profileUsername" class="profile-value">---</span></div>
        <div class="profile-row"><span class="profile-label">Email</span><span id="profileEmail" class="profile-value">---</span></div>
        <div class="profile-row"><span class="profile-label">ID joueur</span><span id="profilePlayerId" class="profile-value">---</span></div>
    </div>
    <div class="rank-panel" id="profileRankSummary">
      <h2>🏆 Nivo ak Tit</h2>
      <div id="profileRankContent">Chaje nivo jwè a…</div>
      <div class="rank-actions"><button type="button" id="openRanksFromProfile">Gade tout nivo yo</button></div>
    </div>
    <button class="back-button" id="profileBack">← Retour</button>
</section>

<!-- NIVO AK TIT / KLASMAN -->
<section id="rankingScreen" class="screen">
  <div class="rank-panel">
    <h1>🏆 Nivo ak Tit MR_Jery</h1>
    <p class="rank-small">Chak viktwa fè w pwoche bò kote pwochen tit la. Sig la parèt bò non jwè a.</p>
    <div id="rankingCurrent" class="rank-current"></div>
    <div class="rank-actions"><button type="button" id="rankingBack">← Retounen</button></div>
    <div style="overflow-x:auto"><table class="rank-table"><thead><tr><th>Nivo</th><th>Tit / Sig</th><th>Viktwa nesesè</th><th>Eta</th></tr></thead><tbody id="rankTableBody"></tbody></table></div>
    <p class="rank-small">Pou kounye a, kantite viktwa sa yo sove nan navigatè aparèy sa a. Pou klasman ofisyèl ant tout jwè yo, sistèm nan dwe konekte ak baz done sèvè a.</p>
  </div>
</section>

<!-- ANNUAIRE DES JOUEURS + NIVEAUX -->
<section id="playersDirectoryScreen" class="screen">
  <div class="rank-panel">
    <h1>👥 Tout jwè yo & 🏆 Nivo yo</h1>
    <p class="rank-small">Lis sa a montre TOUT kont ki enskri sou MR_Jery Morpion, menm lè jwè yo offline. Klasman an baze sou viktwa ki anrejistre nan baz done sèvè a.</p>
    <div class="rank-actions">
      <button type="button" id="playersDirectoryRefresh">🔄 Rafrechi lis jwè yo</button>
      <button type="button" id="playersDirectoryShowRanks">🏆 Gade 30 nivo yo</button>
      <button type="button" id="playersDirectoryBack">← Retounen</button>
    </div>
    <div id="playersDirectoryStatus" class="rank-small" aria-live="polite">Konekte pou chaje lis jwè yo.</div>
    <div style="overflow-x:auto"><table class="rank-table"><thead><tr><th>#</th><th>Jwè</th><th>Sig / Tit</th><th>Viktwa</th><th>Defèt</th><th>Estati</th></tr></thead><tbody id="playersDirectoryBody"><tr><td colspan="6">Konekte sou kont ou epi peze “Rafrechi lis jwè yo”.</td></tr></tbody></table></div>
    <h2 style="margin-top:28px">🏅 Tout 30 nivo MR_Jery yo</h2>
    <p class="rank-small">Sig la parèt bò non jwè a. Nivo a dwe baze sou viktwa ki verifye sou sèvè a pou klasman an valab pou tout moun.</p>
    <div style="overflow-x:auto"><table class="rank-table"><thead><tr><th>Nivo</th><th>Tit / Sig</th><th>Viktwa pou rive</th></tr></thead><tbody id="playersDirectoryRanks"></tbody></table></div>
  </div>
</section>

<!-- PARAMÈTRES -->
<section id="settingsScreen" class="screen">
    <h1>⚙️ Paramètres</h1>
    <div class="settings-box">
        <p>Les paramètres du jeu seront ajoutés ici.</p>
        <p>Pour le moment, aucun réglage supplémentaire n'est nécessaire.</p>
    </div>
    <button class="back-button" id="settingsBack">← Retour</button>
</section>



<!-- PORTEFEUILLE / DEFIS -->
<section id="walletScreen" class="screen">
    <h1>💰 Portefeuille & Défis</h1>
    <div class="wallet-box">
        <div class="notice-test">⚠️ MODE PRÉPARATION : cette version prépare l'interface et les calculs. Aucun argent réel n'est encaissé ou envoyé depuis ce fichier. Le backend et le prestataire de paiement doivent être configurés avant toute activation réelle.</div>
        <div class="wallet-grid">
            <div class="wallet-card"><small>Solde USD</small><strong id="demoUsd">$0.00</strong></div>
            <div class="wallet-card"><small>Solde HTG</small><strong id="demoHtg">0 HTG</strong></div>
            <div class="wallet-card"><small>Commissions plateforme</small><strong id="demoFees">$0.00</strong></div>
        </div>
        <div class="wallet-actions">
            <button id="createBetBtn" class="primary-pay">⚔️ Créer un défi</button>
            <button id="withdrawBtn">💸 Demander un retrait</button>
            <button id="refreshWalletBtn">🔄 Actualiser</button>
        </div>
        <div id="walletMessage" class="account-status"></div>
    </div>

    <div class="bet-box" id="betCreatorBox" style="display:none">
        <h2>⚔️ Nouveau défi</h2>
        <div class="form-row">
            <input id="betOpponent" placeholder="Pseudo de l'adversaire">
            <select id="betCurrency"><option value="USD">USD</option><option value="HTG">HTG</option></select>
        </div>
        <div style="margin-top:10px"><input id="betAmount" type="number" min="0.01" step="0.01" placeholder="Montant de la mise"></div>
        <div class="calc-box">
            <div>Mise joueur 1 : <strong id="calcA">0</strong></div>
            <div>Mise joueur 2 : <strong id="calcB">0</strong></div>
            <div>Total : <strong id="calcTotal">0</strong></div>
            <div>Commission plateforme : <strong id="calcFee">0</strong></div>
            <div>Montant net du gagnant : <strong id="calcWinner">0</strong></div>
        </div>
        <div class="bet-actions">
            <button id="confirmBetBtn" class="primary-pay">Créer le défi</button>
            <button id="cancelBetBtn">Annuler</button>
        </div>
    </div>

    <div class="wallet-box">
        <h2>📜 Historique</h2>
        <div id="walletHistory"><div class="history-item">Aucune transaction en mode test.</div></div>
    </div>
    <button class="back-button" id="walletBack">← Retour</button>
</section>

<!-- ADMIN -->
<section id="adminScreen" class="screen">
    <h1>👑 Administration</h1>
    <div class="admin-box">
        <div class="notice-test">⚠️ Écran de préparation uniquement. Les valeurs réelles doivent être protégées côté serveur, jamais dans le navigateur.</div>
        <div class="wallet-grid">
            <div class="wallet-card"><small>Commission</small><div class="admin-stat" id="adminFee">10%</div></div>
            <div class="wallet-card"><small>Matchs avec mise</small><div class="admin-stat" id="adminMatches">0</div></div>
            <div class="wallet-card"><small>Revenus plateforme</small><div class="admin-stat" id="adminRevenue">$0.00</div></div>
        </div>
        <h2>Paramètres de calcul</h2>
        <div class="form-row">
            <input id="adminCommission" type="number" min="0" max="100" step="0.1" value="10" placeholder="Commission %">
            <button id="saveAdminBtn" class="primary-pay">Enregistrer</button>
        </div>
    </div>
    <button class="back-button" id="adminBack">← Retour</button>
</section>

<!-- ROBOT -->

<section id="robotScreen" class="screen">

    <h1>🤖 Jouer avec Robot — Niveau MASTER</h1>

    <div class="game-info">

        <div id="robotStatus" class="status">
            À ton tour — le robot bloque les victoires immédiates et les trois ouverts.
        </div>

        <div class="timers">

            <div id="robotBlackTimer" class="player-timer active">
                <span class="timer-label">⚫ Noir</span>
                <span id="robotBlackTime" class="timer-value">10:00</span>
            </div>

            <div id="robotRedTimer" class="player-timer">
                <span class="timer-label">🔴 Robot</span>
                <span id="robotRedTime" class="timer-value">10:00</span>
            </div>

        </div>

    </div>

    <div id="robotBoard" class="board-area"></div>

    <div class="game-actions">

        <button class="action-button" id="robotUndo">
            ↩️ Annuler
        </button>

        <button class="action-button" id="robotRestart">
            🔄 Recommencer
        </button>

    </div>

    <button class="back-button" id="robotBack">
        ← Retour
    </button>

</section>

<!-- LOCAL -->

<section id="localScreen" class="screen">

    <h1>👥 2 Utilisateurs</h1>

    <div class="game-info">

        <div id="localStatus" class="status">
            Tour du joueur noir
        </div>

        <div class="timers">

            <div id="localBlackTimer" class="player-timer active">
                <span class="timer-label">⚫ Noir</span>
                <span id="localBlackTime" class="timer-value">10:00</span>
            </div>

            <div id="localRedTimer" class="player-timer">
                <span class="timer-label">🔴 Rouge</span>
                <span id="localRedTime" class="timer-value">10:00</span>
            </div>

        </div>

    </div>

    <div id="localBoard" class="board-area"></div>

    <div class="game-actions">

        <button class="action-button" id="localUndo">
            ↩️ Annuler
        </button>

        <button class="action-button" id="localRestart">
            🔄 Recommencer
        </button>

    </div>

    <button class="back-button" id="localBack">
        ← Retour
    </button>

</section>

<!-- ONLINE MENU -->

<section id="onlineScreen" class="screen">

    <h1>🌐 Jouer en Ligne</h1>

    <div class="online-box">

        <button class="online-choice" id="findOpponentBtn">
            🔎 Trouver un adversaire
        </button>

        <button class="online-choice" id="friendModeBtn">
            👥 Jouer avec un ami
        </button>

        <button class="online-choice" id="waitingRoomBtn">
            ⏳ Salle d'attente
        </button>

        <button class="online-choice" id="spectatorModeBtn">
            👁️ Regarder un match
        </button>

    </div>

    <div id="searchingBox" class="searching-box">

        <div class="searching-message">
            🔎 Recherche d'un adversaire...
        </div>

        <button
            class="cancel-search"
            id="cancelSearchBtn">
            Annuler
        </button>

    </div>

    <div id="friendBox" class="friend-box">

        <input
            id="roomInput"
            type="text"
            maxlength="6"
            placeholder="CODE PARTIE">

        <button id="createBtn">
            Créer une partie
        </button>

        <button id="joinBtn">
            Rejoindre une partie
        </button>

    </div>

    <div id="inviteSettings" class="online-players-box" style="margin-bottom:12px">
        <div class="online-players-title">⚙️ Paramètres de l’invitation</div>
        <div class="invite-settings-grid">
            <label>Durée du match
                <select id="inviteDuration"><option value="1">1 minute</option><option value="2">2 minutes</option><option value="3">3 minutes</option><option value="4">4 minutes</option><option value="5" selected>5 minutes</option><option value="6">6 minutes</option><option value="7">7 minutes</option><option value="8">8 minutes</option><option value="9">9 minutes</option><option value="10">10 minutes</option><option value="11">11 minutes</option><option value="12">12 minutes</option><option value="13">13 minutes</option><option value="14">14 minutes</option><option value="15">15 minutes</option><option value="16">16 minutes</option><option value="17">17 minutes</option><option value="18">18 minutes</option><option value="19">19 minutes</option><option value="20">20 minutes</option><option value="21">21 minutes</option><option value="22">22 minutes</option><option value="23">23 minutes</option><option value="24">24 minutes</option><option value="25">25 minutes</option><option value="26">26 minutes</option><option value="27">27 minutes</option><option value="28">28 minutes</option><option value="29">29 minutes</option><option value="30">30 minutes</option></select>
            </label>
            <label>Gwosè tablo
                <select id="inviteBoardSize"><option value="13">13 × 13</option><option value="14">14 × 14</option><option value="15" selected>15 × 15</option><option value="16">16 × 16</option><option value="17">17 × 17</option><option value="18">18 × 18</option><option value="19">19 × 19</option><option value="20">20 × 20</option></select>
            </label>
        </div>
        <label class="board-style-label">Koulè tablo sou telefòn pa w
            <select id="boardStyleSelect"><option value="classic">Klasik blan</option><option value="midnight">Nuit ble</option><option value="mint">Vèt mant</option><option value="rose">Woz dous</option><option value="sand">Sab klè</option></select>
        </label>
    </div>

    <div id="onlinePlayersBox" class="online-players-box">
        <div class="online-players-title">👥 Joueurs en ligne</div>
        <div id="onlinePlayersList" class="online-players-list"></div>
        <div id="onlinePlayersStatus" class="online-players-status">Chargement des joueurs...</div>
    </div>



    <div class="room">

        Code :
        <span id="roomCode">---</span>

        <br>

        Joueur :
        <span id="playerNumber">---</span>

    </div>

    <div id="onlineError" class="error"></div>

    <button class="back-button" id="onlineBack">
        ← Retour
    </button>

</section>

<!-- SALLE D'ATTENTE -->
<section id="waitingRoomScreen" class="screen">
    <h1>⏳ Salle d'attente</h1>
    <div class="waiting-box">
        <div class="room">Code : <span id="waitingRoomCode">---</span></div>
        <div class="waiting-list">
            <div class="waiting-player">⚫ Joueur 1 : <span id="waitingPlayer1">En attente...</span></div>
            <div class="waiting-player">🔴 Joueur 2 : <span id="waitingPlayer2">En attente...</span></div>
            <div class="waiting-player">👁️ Spectateurs : <span id="waitingSpectatorCount">0</span></div>
        </div>
        <div id="waitingStatus" class="status">En attente...</div>
    </div>
    <button class="back-button" id="waitingBack">← Retour</button>
</section>


<!-- SPECTATEUR -->

<section id="spectatorScreen" class="screen">

    <h1>👁️ Regarder un match</h1>

    <div class="spectator-box">

        <div class="status">Choisissez un match en direct :</div>

        <div id="liveMatchList" class="live-match-list"></div>

        <div id="spectatorError" class="error"></div>

        <button class="account-button" id="refreshSpectatorBtn" type="button">🔄 Actualiser</button>

    </div>

    <button class="back-button" id="spectatorBack">
        ← Retour
    </button>

</section>

<!-- ONLINE GAME -->

<section id="onlineGameScreen" class="screen">

    <h1>🌐 Gomoku en Ligne</h1>

    <div class="game-info">

        <div id="onlineStatus" class="status">
            Connexion...
        </div>

        <div id="onlineMatchNotice" class="online-match-notice"></div>

        <div id="onlineSpectatorCount" class="spectator-count">
            👁️ Spectateurs : 0
        </div>

        <div class="room">

            Code :
            <span id="gameRoomCode">---</span>

        </div>

        <div class="score-board">

            <div class="score-player">
                ⚫ <span id="onlineBlackName">Joueur 1</span> :
                <span id="onlineBlackScore">0</span>
            </div>

            <div class="score-player">
                🔴 <span id="onlineRedName">Joueur 2</span> :
                <span id="onlineRedScore">0</span>
            </div>

        </div>

        <div class="timers">

            <div id="onlineBlackTimer" class="player-timer active">
                <span class="timer-label">⚫ Noir</span>
                <span id="onlineBlackTime" class="timer-value">10:00</span>
            </div>

            <div id="onlineRedTimer" class="player-timer">
                <span class="timer-label">🔴 Rouge</span>
                <span id="onlineRedTime" class="timer-value">10:00</span>
            </div>

        </div>

        <div id="onlineResult" class="online-result"></div>

        <div id="rematchBox" class="rematch-box">

            <div
                id="rematchMessage"
                class="rematch-message">
            </div>

            <div
                id="rematchActions"
                class="rematch-actions">
            </div>

        </div>

        <div id="undoBox" class="rematch-box undo-box">

            <div id="undoMessage" class="rematch-message"></div>

            <div id="undoActions" class="rematch-actions"></div>

        </div>

    </div>

    <div id="onlineBoard" class="board-area"></div>

    <!-- Chat en direct + communication vocale -->
    <section id="matchCommunication" class="match-communication" aria-label="Chat du match">
      <div class="match-comm-header">
        <h3>💬 Chat du match</h3>
        <button type="button" id="toggleMatchChat" class="match-comm-toggle">Masquer</button>
      </div>
      <div id="matchChatBody">
        <div id="matchChatMessages" class="match-chat-messages" aria-live="polite"></div>
        <form id="matchChatForm" class="match-chat-form">
          <input id="matchChatInput" type="text" maxlength="300" placeholder="Ekri mesaj ou..." autocomplete="off" aria-label="Mesaj chat" />
          <button type="submit">Voye</button>
        </form>
      </div>
      <div class="match-voice-controls">
        <button type="button" id="matchMicButton">🎤 Aktive mikwo</button>
        <button type="button" id="muteAllSpectatorsButton">🔇 Mute tout spektatè</button>
        <span id="matchVoiceStatus" role="status">Mikwo fèmen</span>
      </div>
      <div id="matchVoicePeerControls" class="match-voice-controls" aria-label="Kontwòl vwa chak moun"></div>
      <div id="matchRemoteAudios"></div>
      <audio id="matchRemoteAudio" autoplay playsinline></audio>
      <div class="match-comm-note">Jwè ak spektatè ka pale. Kontwòl mute yo afekte aparèy pa w sèlman.</div>
    </section>

    <div class="game-actions">

        <button
            class="action-button"
            id="onlineNewGame"
            style="display:none;">
            🔄 Nouvelle partie
        </button>

    </div>

    <div id="gameOnlineError" class="error"></div>

    <div class="game-actions" style="margin-top:10px">
        <button class="back-button" id="leaveOnlineMatchBtn" type="button" style="background:#991b1b;border-color:#ef4444">🚪 Kite match la</button>
    </div>

    <button class="back-button" id="onlineGameBack">
        ← Retour au menu
    </button>

</section>

<!-- Invitation rete vizib menm lè jwè a kite ekran match la -->
<div id="gameInviteBox" class="game-invite-box" role="dialog" aria-live="polite" aria-label="Invitation match">
    <div id="gameInviteMessage" class="game-invite-message"></div>
    <div class="game-invite-actions">
        <button id="acceptGameInviteBtn" class="invite-accept" type="button">✅ Accepter</button>
        <button id="refuseGameInviteBtn" class="invite-refuse" type="button">❌ Refuser</button>
    </div>
</div>

<!-- ÉCRAN VICTOIRE LOCAL / ROBOT -->

<section id="winScreen" class="screen">

    <h1 class="win-title">
        🏆 FIN DE PARTIE
    </h1>

    <div
        id="winMessage"
        class="win-message">
    </div>

    <div class="win-buttons">

        <button
            class="menu-button"
            id="winRestart">
            🔄 Rejouer
        </button>

        <button
            class="back-button"
            id="winMenu">
            ← Retour au menu
        </button>

    </div>

</section>

</div>

<script>

/* ==================================================
   SERVEUR
================================================== */

const SERVER_URL =
    "wss://gomoku-server-5h60.onrender.com";

let BOARD_SIZE = 20;
const START_TIME = 10 * 60;

/* ==================================================
   COMPTE JOUEUR
================================================== */

let currentPlayerId = null;
let currentUsername = null;
let currentEmail = null;
let accountToken = null;
let accountConnected = false;
let accountRequestInProgress = false;
let onlineOpenedFromAccountMenu = false;
let pendingRestoreCallback = null;
// Garde les actions demandées pendant que le WebSocket est encore en cours d'ouverture.
let pendingConnectionCallbacks = [];
function runPendingConnectionCallbacks() {
    const callbacks = pendingConnectionCallbacks.splice(0);
    callbacks.forEach(function(fn) {
        if (typeof fn === "function") {
            try { fn(); } catch (e) { console.error("Erreur action après connexion", e); }
        }
    });
}
let restoreSessionTimeout = null;
let restoringAccountSession = false;

function showAccountMessage(message, success) {
    const box = document.getElementById("accountStatus");
    if (!box) return;
    box.textContent = message || "";
    box.style.color = success ? "#86EFAC" : "#FCA5A5";
}

function updateAccountDisplay() {
    const user = document.getElementById("accountUser");
    if (user) {
        user.textContent = accountConnected
            ? "👤 Connecté : " + currentUsername
            : "";
    }
}

function showAccountMenu() {
    const user = document.getElementById("accountMenuUser");
    if (user) {
        user.textContent = accountConnected
            ? "👤 Connecté : " + currentUsername
            : "";
    }
    refreshDashboardUser();
    showScreen("accountMenuScreen");
}


/* ==================================================
   DASHBOARD APRÈS CONNEXION
================================================== */
function applyBoardStyle(style){
  const allowed=["classic","midnight","mint","rose","sand"];
  const chosen=allowed.includes(style)?style:"classic";
  document.body.classList.remove(...allowed.map(x=>"board-style-"+x));
  if(chosen!=="classic") document.body.classList.add("board-style-"+chosen);
  const select=document.getElementById("boardStyleSelect"); if(select) select.value=chosen;
  try{localStorage.setItem("mrjery_board_style",chosen);}catch(e){}
}
try{applyBoardStyle(localStorage.getItem("mrjery_board_style")||"classic");}catch(e){applyBoardStyle("classic");}
document.getElementById("boardStyleSelect")?.addEventListener("change",e=>applyBoardStyle(e.target.value));

function refreshDashboardUser(){
  const u=document.getElementById('dashboardUsername'); if(u) u.textContent=currentUsername||'Joueur';
  const au=document.getElementById('accountMenuUser'); if(au) au.textContent='👤 '+(currentUsername||'Connecté');
  try { if(typeof mrjeryUpdateRankDisplays==='function') mrjeryUpdateRankDisplays(); } catch(e) {}
}

function openWalletFromDashboard(){ showScreen('walletScreen'); }
document.getElementById('walletTopBtn')?.addEventListener('click',openWalletFromDashboard);
document.getElementById('adminTopBtn')?.addEventListener('click',function(){
  showScreen('adminScreen');
  renderWallet();
});
document.getElementById('adminBack')?.addEventListener('click',function(){showAccountMenu();});
document.getElementById('dashboardBetCard')?.addEventListener('click',openWalletFromDashboard);
document.getElementById('dashboardChallengeCard')?.addEventListener('click',openWalletFromDashboard);
document.getElementById('dashboardOnlineCard')?.addEventListener('click',()=>document.getElementById('accountOnlineBtn')?.click());
document.getElementById('dashboardFriendCard')?.addEventListener('click',()=>document.getElementById('accountOnlineBtn')?.click());
document.getElementById('dashboardRobotCard')?.addEventListener('click',()=>{
  // Ouvrir directement le jeu contre le robot : ne pas passer par l'écran 2 utilisateurs.
  stopAllTimers();
  resetRobotGame();
  showScreen('robotScreen');
});
document.getElementById('dashboardSpectatorCard')?.addEventListener('click',()=>document.getElementById('accountOnlineBtn')?.click());
document.getElementById('dashboardRankingBtn')?.addEventListener('click',openRankingScreen);
document.getElementById('dashboardRankingCard')?.addEventListener('click',()=>document.getElementById('dashboardRankingBtn')?.click());
document.getElementById('dashboardDepositUsd')?.addEventListener('click',openWalletFromDashboard);
document.getElementById('dashboardDepositHtg')?.addEventListener('click',openWalletFromDashboard);


// JERY GAMES menu: the existing Morpion flow is reused; other games are clearly marked as not yet released.
document.getElementById('dashboardGamesCard')?.addEventListener('click',()=>showScreen('jeryGamesScreen'));
document.getElementById('jeryGamesBack')?.addEventListener('click',()=>showScreen('accountMenuScreen'));
document.getElementById('jeryGamesGrid')?.addEventListener('click',function(e){
  const card=e.target.closest('[data-game]'); if(!card)return;
  if(card.dataset.game==='morpion'){
    showScreen('accountMenuScreen');
    document.getElementById('dashboardOnlineCard')?.focus();
    return;
  }
  const label=card.querySelector('strong')?.textContent||'Jwèt sa a';
  alert(label+' ap vini byento. Nou poko aktive jwèt sa a; jwèt ki deja la yo pa chanje.');
});

/* ==================================================
   ÉCRANS
================================================== */

const screens =
    document.querySelectorAll(".screen");

function showScreen(id) {

    screens.forEach(function(screen) {
        screen.classList.remove("active");
    });

    const target =
        document.getElementById(id);

    if (target) {
        target.classList.add("active");
    }

    window.scrollTo(0, 0);
}

/* ==================================================
   TABLEAU
================================================== */

function createBoard(container, clickFunction) {

    container.innerHTML = "";

    const empty =
        document.createElement("div");

    container.appendChild(empty);

    const letters =
        document.createElement("div");

    letters.className = "letters";
    letters.style.gridTemplateColumns = `repeat(${BOARD_SIZE}, minmax(0, 1fr))`;

    for (let i = 0; i < BOARD_SIZE; i++) {

        const letter =
            document.createElement("span");

        letter.textContent =
            String.fromCharCode(65 + i);

        letters.appendChild(letter);
    }

    container.appendChild(letters);

    const numbers =
        document.createElement("div");

    numbers.className = "numbers";
    numbers.style.gridTemplateRows = `repeat(${BOARD_SIZE}, minmax(0, 1fr))`;

    for (let i = 1; i <= BOARD_SIZE; i++) {

        const number =
            document.createElement("span");

        number.textContent = i;

        numbers.appendChild(number);
    }

    container.appendChild(numbers);

    const board =
        document.createElement("div");

    board.className = "board";
    // The selected board size controls the exact number of playable intersections.
    board.style.gridTemplateColumns = `repeat(${BOARD_SIZE}, minmax(0, 1fr))`;
    board.style.gridTemplateRows = `repeat(${BOARD_SIZE}, minmax(0, 1fr))`;

    for (let row = 0; row < BOARD_SIZE; row++) {

        for (let col = 0; col < BOARD_SIZE; col++) {

            const cell =
                document.createElement("div");

            cell.className = "cell";

            cell.dataset.row = row;
            cell.dataset.col = col;

            cell.addEventListener(
                "click",
                function() {

                    clickFunction(
                        row,
                        col,
                        cell
                    );

                }
            );

            board.appendChild(cell);
        }
    }

    const svg =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "svg"
        );

    svg.classList.add(
        "winning-line-svg"
    );

    svg.setAttribute(
        "viewBox",
        "0 0 100 100"
    );

    svg.setAttribute(
        "preserveAspectRatio",
        "none"
    );

    const line =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "line"
        );

    line.setAttribute("x1", "0");
    line.setAttribute("y1", "0");
    line.setAttribute("x2", "0");
    line.setAttribute("y2", "0");

    line.style.display = "none";

    svg.appendChild(line);

    board.appendChild(svg);

    container.appendChild(board);
}

/* ==================================================
   PION
================================================== */

function drawStone(cell, color) {

    if (!cell) {
        return;
    }

    cell.innerHTML = "";

    const stone =
        document.createElement("div");

    stone.className =
        "stone " + color;

    cell.appendChild(stone);
}

/* ==================================================
   LIGN VICTOIRE
================================================== */

function drawWinningLine(
    containerId,
    winningLine
) {

    const container =
        document.getElementById(
            containerId
        );

    if (!container) {
        return;
    }

    const board =
        container.querySelector(
            ".board"
        );

    if (!board) {
        return;
    }

    const svg =
        board.querySelector(
            ".winning-line-svg"
        );

    const line =
        svg
            ? svg.querySelector("line")
            : null;

    if (!svg || !line) {
        return;
    }

    line.style.display = "none";

    if (
        !Array.isArray(winningLine) ||
        winningLine.length !== 5
    ) {
        return;
    }

    const first =
        winningLine[0];

    const last =
        winningLine[4];

    const x1 =
        ((Number(first.col) + 0.5) /
            BOARD_SIZE) * 100;

    const y1 =
        ((Number(first.row) + 0.5) /
            BOARD_SIZE) * 100;

    const x2 =
        ((Number(last.col) + 0.5) /
            BOARD_SIZE) * 100;

    const y2 =
        ((Number(last.row) + 0.5) /
            BOARD_SIZE) * 100;

    line.setAttribute(
        "x1",
        x1
    );

    line.setAttribute(
        "y1",
        y1
    );

    line.setAttribute(
        "x2",
        x2
    );

    line.setAttribute(
        "y2",
        y2
    );

    line.style.display = "block";
}

function clearWinningLine(containerId) {

    const container =
        document.getElementById(
            containerId
        );

    if (!container) {
        return;
    }

    const line =
        container.querySelector(
            ".winning-line-svg line"
        );

    if (line) {
        line.style.display = "none";
    }
}

/* ==================================================
   TIMER
================================================== */

let localBlackTime = START_TIME;
let localRedTime = START_TIME;

let robotBlackTime = START_TIME;
let robotRedTime = START_TIME;

let localTimerInterval = null;
let robotTimerInterval = null;

/* ==================================================
   FORMAT TIMER
================================================== */

function formatTime(seconds) {

    seconds = Math.max(
        0,
        Math.floor(
            Number(seconds) || 0
        )
    );

    const minutes =
        Math.floor(seconds / 60);

    const remainingSeconds =
        seconds % 60;

    return (
        String(minutes).padStart(2, "0") +
        ":" +
        String(remainingSeconds).padStart(2, "0")
    );
}

/* ==================================================
   LOCAL
================================================== */

let localBoard = {};
let localTurn = "black";
let localGameOver = false;
let localHistory = [];

function updateLocalTimers() {

    document
        .getElementById("localBlackTime")
        .textContent =
        formatTime(localBlackTime);

    document
        .getElementById("localRedTime")
        .textContent =
        formatTime(localRedTime);

    const blackBox =
        document.getElementById(
            "localBlackTimer"
        );

    const redBox =
        document.getElementById(
            "localRedTimer"
        );

    blackBox.classList.toggle(
        "active",
        localTurn === "black" &&
        !localGameOver
    );

    redBox.classList.toggle(
        "active",
        localTurn === "red" &&
        !localGameOver
    );

    blackBox.classList.toggle(
        "warning",
        localBlackTime <= 60
    );

    redBox.classList.toggle(
        "warning",
        localRedTime <= 60
    );
}

function startLocalTimer() {

    stopLocalTimer();

    localTimerInterval =
        setInterval(function() {

            if (localGameOver) {
                return;
            }

            if (localTurn === "black") {

                localBlackTime--;

                if (localBlackTime <= 0) {

                    localBlackTime = 0;
                    localGameOver = true;

                    updateLocalTimers();
                    stopLocalTimer();

                    showWinScreen(
                        "🔴 Le joueur rouge gagne ! Le temps du joueur noir est écoulé."
                    );

                    return;
                }

            } else {

                localRedTime--;

                if (localRedTime <= 0) {

                    localRedTime = 0;
                    localGameOver = true;

                    updateLocalTimers();
                    stopLocalTimer();

                    showWinScreen(
                        "⚫ Le joueur noir gagne ! Le temps du joueur rouge est écoulé."
                    );

                    return;
                }
            }

            updateLocalTimers();

        }, 1000);

    updateLocalTimers();
}

function stopLocalTimer() {

    if (localTimerInterval) {

        clearInterval(
            localTimerInterval
        );

        localTimerInterval = null;
    }
}

function resetLocalGame() {

    stopLocalTimer();

    localBoard = {};
    localTurn = "black";
    localGameOver = false;
    localHistory = [];

    localBlackTime = START_TIME;
    localRedTime = START_TIME;

    document
        .getElementById("localStatus")
        .textContent =
        "Tour du joueur noir";

    createBoard(
        document.getElementById(
            "localBoard"
        ),
        localClick
    );

    updateLocalTimers();
    startLocalTimer();
}

function localClick(row, col, cell) {

    if (localGameOver) {
        return;
    }

    const key =
        row + "," + col;

    if (localBoard[key]) {
        return;
    }

    localHistory.push({
        row: row,
        col: col,
        color: localTurn
    });

    localBoard[key] =
        localTurn;

    drawStone(
        cell,
        localTurn
    );

    if (
        checkWin(
            localBoard,
            row,
            col,
            localTurn
        )
    ) {

        localGameOver = true;

        showWinScreen(
            localTurn === "black"
                ? "⚫ Le joueur noir a gagné !"
                : "🔴 Le joueur rouge a gagné !"
        );

        return;
    }

    if (
        Object.keys(localBoard).length >= 400
    ) {

        localGameOver = true;

        showWinScreen(
            "🤝 Match nul !"
        );

        return;
    }

    localTurn =
        localTurn === "black"
            ? "red"
            : "black";

    document
        .getElementById("localStatus")
        .textContent =
        localTurn === "black"
            ? "Tour du joueur noir"
            : "Tour du joueur rouge";

    updateLocalTimers();
}

function undoLocal() {

    if (localHistory.length === 0) {
        return;
    }

    const last =
        localHistory.pop();

    delete localBoard[
        last.row + "," + last.col
    ];

    localTurn =
        last.color;

    localGameOver = false;

    createBoard(
        document.getElementById(
            "localBoard"
        ),
        localClick
    );

    renderLocalBoard();

    document
        .getElementById("localStatus")
        .textContent =
        localTurn === "black"
            ? "Tour du joueur noir"
            : "Tour du joueur rouge";

    updateLocalTimers();
    startLocalTimer();
}

function renderLocalBoard() {

    const boardElement =
        document.querySelector(
            "#localBoard .board"
        );

    if (!boardElement) {
        return;
    }

    for (const key in localBoard) {

        const parts =
            key.split(",");

        const row =
            Number(parts[0]);

        const col =
            Number(parts[1]);

        const index =
            row * BOARD_SIZE + col;

        drawStone(
            boardElement.children[index],
            localBoard[key]
        );
    }
}

/* ==================================================
   ROBOT
================================================== */

let robotBoard = {};
let robotTurn = "black";
let robotGameOver = false;
let robotHistory = [];

function updateRobotTimers() {

    document
        .getElementById("robotBlackTime")
        .textContent =
        formatTime(robotBlackTime);

    document
        .getElementById("robotRedTime")
        .textContent =
        formatTime(robotRedTime);

    const blackBox =
        document.getElementById(
            "robotBlackTimer"
        );

    const redBox =
        document.getElementById(
            "robotRedTimer"
        );

    blackBox.classList.toggle(
        "active",
        robotTurn === "black" &&
        !robotGameOver
    );

    redBox.classList.toggle(
        "active",
        robotTurn === "red" &&
        !robotGameOver
    );

    blackBox.classList.toggle(
        "warning",
        robotBlackTime <= 60
    );

    redBox.classList.toggle(
        "warning",
        robotRedTime <= 60
    );
}

function startRobotTimer() {

    stopRobotTimer();

    robotTimerInterval =
        setInterval(function() {

            if (robotGameOver) {
                return;
            }

            if (robotTurn === "black") {

                robotBlackTime--;

                if (robotBlackTime <= 0) {

                    robotBlackTime = 0;
                    robotGameOver = true;

                    updateRobotTimers();
                    stopRobotTimer();

                    showWinScreen(
                        "🤖 Le robot gagne ! Ton temps est écoulé."
                    );

                    return;
                }

            } else {

                robotRedTime--;

                if (robotRedTime <= 0) {

                    robotRedTime = 0;
                    robotGameOver = true;

                    updateRobotTimers();
                    stopRobotTimer();

                    showWinScreen(
                        "⚫ Tu gagnes ! Le temps du robot est écoulé."
                    );

                    return;
                }
            }

            updateRobotTimers();

        }, 1000);

    updateRobotTimers();
}

function stopRobotTimer() {

    if (robotTimerInterval) {

        clearInterval(
            robotTimerInterval
        );

        robotTimerInterval = null;
    }
}

function resetRobotGame() {

    stopRobotTimer();

    robotBoard = {};
    robotTurn = "black";
    robotGameOver = false;
    robotHistory = [];

    robotBlackTime = START_TIME;
    robotRedTime = START_TIME;

    document
        .getElementById("robotStatus")
        .textContent =
        "À ton tour";

    createBoard(
        document.getElementById(
            "robotBoard"
        ),
        robotClick
    );

    updateRobotTimers();
    startRobotTimer();
}

function robotClick(row, col, cell) {

    if (robotGameOver) {
        return;
    }

    if (robotTurn !== "black") {
        return;
    }

    const key =
        row + "," + col;

    if (robotBoard[key]) {
        return;
    }

    robotHistory.push({
        row: row,
        col: col,
        color: "black"
    });

    robotBoard[key] =
        "black";

    drawStone(
        cell,
        "black"
    );

    if (
        checkWin(
            robotBoard,
            row,
            col,
            "black"
        )
    ) {

        robotGameOver = true;

        showWinScreen(
            "⚫ Tu as gagné !"
        );

        return;
    }

    robotTurn = "red";

    document
        .getElementById("robotStatus")
        .textContent =
        "🤖 Le robot réfléchit...";

    updateRobotTimers();

    setTimeout(
        robotMove,
        350
    );
}

function robotMove() {

    if (robotGameOver) {
        return;
    }

    const bestMove =
        findBestRobotMove();

    if (!bestMove) {
        return;
    }

    const row =
        bestMove.row;

    const col =
        bestMove.col;

    const key =
        row + "," + col;

    robotHistory.push({
        row: row,
        col: col,
        color: "red"
    });

    robotBoard[key] =
        "red";

    const boardElement =
        document.querySelector(
            "#robotBoard .board"
        );

    const index =
        row * BOARD_SIZE + col;

    const cell =
        boardElement.children[index];

    drawStone(
        cell,
        "red"
    );

    if (
        checkWin(
            robotBoard,
            row,
            col,
            "red"
        )
    ) {

        robotGameOver = true;

        showWinScreen(
            "🤖 Le robot a gagné !"
        );

        return;
    }

    if (
        Object.keys(robotBoard).length >= 400
    ) {

        robotGameOver = true;

        showWinScreen(
            "🤝 Match nul !"
        );

        return;
    }

    robotTurn = "black";

    document
        .getElementById("robotStatus")
        .textContent =
        "À ton tour";

    updateRobotTimers();
}

function findOpenThreeBlockMove(color = "black") {
    // Bloke yon 3 pyon youn dèyè lòt ki gen espas vid nan toude bout yo (_BBB_).
    // Sa anpeche advèsè a kontinye bati yon kat pyon ouvè.
    const dirs = [[1,0],[0,1],[1,1],[1,-1]];
    for (const [dr, dc] of dirs) {
        for (let row = 0; row < BOARD_SIZE; row++) {
            for (let col = 0; col < BOARD_SIZE; col++) {
                const r1=row+dr, c1=col+dc;
                const r2=row+2*dr, c2=col+2*dc;
                const r3=row+3*dr, c3=col+3*dc;
                const r4=row+4*dr, c4=col+4*dc;
                if ([r1,c1,r2,c2,r3,c3,r4,c4].some(v=>!Number.isInteger(v))) continue;
                if (row<0 || row>=BOARD_SIZE || col<0 || col>=BOARD_SIZE ||
                    r1<0 || r1>=BOARD_SIZE || c1<0 || c1>=BOARD_SIZE ||
                    r2<0 || r2>=BOARD_SIZE || c2<0 || c2>=BOARD_SIZE ||
                    r3<0 || r3>=BOARD_SIZE || c3<0 || c3>=BOARD_SIZE ||
                    r4<0 || r4>=BOARD_SIZE || c4<0 || c4>=BOARD_SIZE) continue;
                const start = row+','+col;
                if (robotBoard[start]) continue;
                if (robotBoard[r1+','+c1]===color && robotBoard[r2+','+c2]===color &&
                    robotBoard[r3+','+c3]===color && !robotBoard[r4+','+c4]) {
                    return {row, col};
                }
            }
        }
    }
    return null;
}

function findBestRobotMove() {
    // Niveau MASTER : priorité absolue à une victoire immédiate, puis au blocage
    // d'une victoire adverse. Ensuite, évalue les attaques ET les défenses/fourches.
    const winNow = findWinningMove("red");
    if (winNow) return winNow;

    const mustBlock = findWinningMove("black");
    if (mustBlock) return mustBlock;

    // Priorite défensive supplémentaire : ne laisse pas l'adversaire garder un trois ouvert.
    const blockOpenThree = findOpenThreeBlockMove("black");
    if (blockOpenThree) return blockOpenThree;

    const occupied = Object.keys(robotBoard);
    const center = Math.floor(BOARD_SIZE / 2);
    if (!occupied.length) return { row: center, col: center };

    const candidates = new Map();
    for (const item of occupied) {
        const [r0, c0] = item.split(",").map(Number);
        for (let dr = -2; dr <= 2; dr++) {
            for (let dc = -2; dc <= 2; dc++) {
                const row = r0 + dr, col = c0 + dc;
                if (row < 0 || row >= BOARD_SIZE || col < 0 || col >= BOARD_SIZE) continue;
                const key = row + "," + col;
                if (!robotBoard[key]) candidates.set(key, { row, col });
            }
        }
    }

    let best = null;
    let bestScore = -Infinity;
    for (const move of candidates.values()) {
        const key = move.row + "," + move.col;
        // Simule une attaque du robot puis une défense du joueur : les menaces
        // ouvertes et les alignements de 3/4 pions reçoivent un poids élevé.
        robotBoard[key] = "red";
        const attack = scoreMasterPosition(move.row, move.col, "red");
        const redForks = countWinningMoves("red", 2);
        delete robotBoard[key];

        robotBoard[key] = "black";
        const defense = scoreMasterPosition(move.row, move.col, "black");
        const blackForks = countWinningMoves("black", 2);
        delete robotBoard[key];

        const distance = Math.abs(move.row - center) + Math.abs(move.col - center);
        const centerBonus = Math.max(0, 16 - distance * 0.45);
        const score = attack * 1.15 + defense * 1.10 + redForks * 24000 - blackForks * 30000 + centerBonus;
        if (score > bestScore) { bestScore = score; best = move; }
    }
    return best || { row: center, col: center };
}

function countWinningMoves(color, stopAt = 2) {
    let count = 0;
    for (let row = 0; row < BOARD_SIZE; row++) {
        for (let col = 0; col < BOARD_SIZE; col++) {
            const key = row + ',' + col;
            if (robotBoard[key]) continue;
            robotBoard[key] = color;
            const wins = checkWin(robotBoard, row, col, color);
            delete robotBoard[key];
            if (wins && ++count >= stopAt) return count;
        }
    }
    return count;
}

function scoreMasterPosition(row, col, color) {
    const directions = [[1,0],[0,1],[1,1],[1,-1]];
    let total = 0;
    for (const [dr, dc] of directions) {
        let count = 1, open = 0;
        for (const sign of [-1, 1]) {
            let r = row + dr * sign, c = col + dc * sign;
            while (r >= 0 && r < BOARD_SIZE && c >= 0 && c < BOARD_SIZE && robotBoard[r + ',' + c] === color) {
                count++; r += dr * sign; c += dc * sign;
            }
            if (r >= 0 && r < BOARD_SIZE && c >= 0 && c < BOARD_SIZE && !robotBoard[r + ',' + c]) open++;
        }
        // 4+ : urgence; 3 ouverts : menace à bloquer/créer; 2 : préparation.
        if (count >= 5) total += 100000;
        else if (count === 4 && open === 2) total += 18000;
        else if (count === 4 && open === 1) total += 9000;
        else if (count === 3 && open === 2) total += 2400;
        else if (count === 3 && open === 1) total += 650;
        else if (count === 2 && open === 2) total += 180;
        else if (count === 2 && open === 1) total += 45;
        else total += count * 4;
    }
    return total;
}

function findWinningMove(color) {

    for (
        let row = 0;
        row < BOARD_SIZE;
        row++
    ) {

        for (
            let col = 0;
            col < BOARD_SIZE;
            col++
        ) {

            const key =
                row + "," + col;

            if (robotBoard[key]) {
                continue;
            }

            robotBoard[key] =
                color;

            const win =
                checkWin(
                    robotBoard,
                    row,
                    col,
                    color
                );

            delete robotBoard[key];

            if (win) {

                return {
                    row: row,
                    col: col
                };
            }
        }
    }

    return null;
}

function evaluatePosition(
    row,
    col,
    color
) {

    let score = 0;

    const center = 9.5;

    const distance =
        Math.abs(row - center) +
        Math.abs(col - center);

    score += 30 - distance;

    const directions = [
        [1, 0],
        [0, 1],
        [1, 1],
        [1, -1]
    ];

    for (const direction of directions) {

        const dr = direction[0];
        const dc = direction[1];

        let count = 0;

        for (
            let step = 1;
            step <= 4;
            step++
        ) {

            const r =
                row + dr * step;

            const c =
                col + dc * step;

            if (
                r < 0 ||
                r >= BOARD_SIZE ||
                c < 0 ||
                c >= BOARD_SIZE
            ) {
                break;
            }

            const key =
                r + "," + c;

            if (
                robotBoard[key] === color
            ) {

                count++;

            } else {

                break;
            }
        }

        score += count * 20;
    }

    return score;
}

function undoRobot() {

    if (robotHistory.length === 0) {
        return;
    }

    const lastRobot =
        robotHistory.pop();

    delete robotBoard[
        lastRobot.row + "," +
        lastRobot.col
    ];

    if (robotHistory.length > 0) {

        const lastPlayer =
            robotHistory.pop();

        delete robotBoard[
            lastPlayer.row + "," +
            lastPlayer.col
        ];
    }

    robotTurn = "black";
    robotGameOver = false;

    createBoard(
        document.getElementById(
            "robotBoard"
        ),
        robotClick
    );

    renderRobotBoard();

    document
        .getElementById("robotStatus")
        .textContent =
        "À ton tour";

    updateRobotTimers();
    startRobotTimer();
}

function renderRobotBoard() {

    const boardElement =
        document.querySelector(
            "#robotBoard .board"
        );

    if (!boardElement) {
        return;
    }

    for (const key in robotBoard) {

        const parts =
            key.split(",");

        const row =
            Number(parts[0]);

        const col =
            Number(parts[1]);

        const index =
            row * BOARD_SIZE + col;

        drawStone(
            boardElement.children[index],
            robotBoard[key]
        );
    }
}

/* ==================================================
   EXACTEMENT 5
================================================== */

function checkWin(
    board,
    row,
    col,
    color
) {

    const directions = [
        [1, 0],
        [0, 1],
        [1, 1],
        [1, -1]
    ];

    for (const direction of directions) {

        const dr = direction[0];
        const dc = direction[1];

        let count = 1;

        let r =
            row + dr;

        let c =
            col + dc;

        while (
            r >= 0 &&
            r < BOARD_SIZE &&
            c >= 0 &&
            c < BOARD_SIZE &&
            board[
                r + "," + c
            ] === color
        ) {

            count++;

            r += dr;
            c += dc;
        }

        r =
            row - dr;

        c =
            col - dc;

        while (
            r >= 0 &&
            r < BOARD_SIZE &&
            c >= 0 &&
            c < BOARD_SIZE &&
            board[
                r + "," + c
            ] === color
        ) {

            count++;

            r -= dr;
            c -= dc;
        }

        if (count === 5) {
            return true;
        }
    }

    return false;
}

/* ==================================================
   VICTOIRE LOCAL / ROBOT
================================================== */

// SYSTEME DE NIVEAUX ET SIGLES — 30 rangs basés sur les victoires.
const MRJERY_RANKS = [
 {n:1,title:'Débutant',sig:'DBT',wins:0,color:'#9ca3af',en:'Beginner',ht:'Debitan'},
 {n:2,title:'Apprenti',sig:'APP',wins:3,color:'#a8b0bd',en:'Apprentice',ht:'Apranti'},
 {n:3,title:'Joueur',sig:'JOU',wins:8,color:'#d1d5db',en:'Player',ht:'Jwè'},
 {n:4,title:'Combattant',sig:'CMB',wins:15,color:'#86efac',en:'Fighter',ht:'Konbatan'},
 {n:5,title:'Stratège',sig:'STR',wins:25,color:'#4ade80',en:'Strategist',ht:'Estratej'},
 {n:6,title:'Tacticien',sig:'TAC',wins:40,color:'#34d399',en:'Tactician',ht:'Taktisyen'},
 {n:7,title:'Expert',sig:'EXP',wins:60,color:'#22d3ee',en:'Expert',ht:'Ekspè'},
 {n:8,title:'Expert confirmé',sig:'EXC',wins:85,color:'#38bdf8',en:'Skilled Expert',ht:'Ekspè konfime'},
 {n:9,title:'Maître tactique',sig:'MT',wins:115,color:'#60a5fa',en:'Tactical Master',ht:'Mèt taktik'},
 {n:10,title:'Maître',sig:'MTR',wins:150,color:'#818cf8',en:'Master',ht:'Mèt'},
 {n:11,title:'Maître avancé',sig:'MTA',wins:190,color:'#a78bfa',en:'Advanced Master',ht:'Mèt avanse'},
 {n:12,title:'Maître supérieur',sig:'MTS',wins:235,color:'#c084fc',en:'Senior Master',ht:'Mèt siperyè'},
 {n:13,title:'Champion',sig:'CH',wins:285,color:'#e879f9',en:'Champion',ht:'Chanpyon'},
 {n:14,title:'Champion confirmé',sig:'CHC',wins:340,color:'#f472b6',en:'Proven Champion',ht:'Chanpyon konfime'},
 {n:15,title:'Champion élite',sig:'CHE',wins:400,color:'#fb7185',en:'Elite Champion',ht:'Chanpyon elit'},
 {n:16,title:'Grand Champion',sig:'GC',wins:470,color:'#f87171',en:'Grand Champion',ht:'Gran chanpyon'},
 {n:17,title:'Maître d’élite',sig:'ME',wins:550,color:'#fb923c',en:'Elite Master',ht:'Mèt elit'},
 {n:18,title:'Maître légendaire',sig:'ML',wins:640,color:'#fbbf24',en:'Legendary Master',ht:'Mèt lejandè'},
 {n:19,title:'Élite suprême',sig:'ES',wins:740,color:'#facc15',en:'Supreme Elite',ht:'Elit siprèm'},
 {n:20,title:'Grand Maître',sig:'GM',wins:850,color:'#fde047',en:'Grandmaster',ht:'Gran Mèt'},
 {n:21,title:'Grand Maître confirmé',sig:'GMC',wins:975,color:'#bef264',en:'Senior Grandmaster',ht:'Gran Mèt konfime'},
 {n:22,title:'Grand Maître d’élite',sig:'GME',wins:1110,color:'#a3e635',en:'Elite Grandmaster',ht:'Gran Mèt elit'},
 {n:23,title:'Maître international',sig:'MI',wins:1260,color:'#4ade80',en:'International Master',ht:'Mèt entènasyonal'},
 {n:24,title:'Grand Maître international',sig:'GMI',wins:1425,color:'#2dd4bf',en:'International Grandmaster',ht:'Gran Mèt entènasyonal'},
 {n:25,title:'Légende',sig:'LEG',wins:1605,color:'#22d3ee',en:'Legend',ht:'Lejand'},
 {n:26,title:'Légende suprême',sig:'LS',wins:1800,color:'#38bdf8',en:'Supreme Legend',ht:'Lejand siprèm'},
 {n:27,title:'Icône',sig:'ICO',wins:2020,color:'#60a5fa',en:'Icon',ht:'Ikòn'},
 {n:28,title:'Icône mondiale',sig:'IM',wins:2260,color:'#818cf8',en:'World Icon',ht:'Ikòn mondyal'},
 {n:29,title:'Immortel',sig:'IMM',wins:2525,color:'#c084fc',en:'Immortal',ht:'Imòtèl'},
 {n:30,title:'Légende MR_Jery',sig:'LMJ',wins:2800,color:'#f5bd32',en:'MR_Jery Legend',ht:'Lejand MR_Jery'}
];
function mrjeryRankStorageKey(){return 'mrjery_rank_stats_'+String(currentUsername||currentPlayerId||'guest').toLowerCase().replace(/[^a-z0-9_-]/g,'_');}
function mrjeryGetWins(){try{return Math.max(0,Number(JSON.parse(localStorage.getItem(mrjeryRankStorageKey())||'{}').wins)||0)}catch(e){return 0}}
function mrjeryCurrentRank(wins=mrjeryGetWins()){let r=MRJERY_RANKS[0];for(const x of MRJERY_RANKS){if(wins>=x.wins)r=x;else break;}return r;}
function mrjeryRankLabel(r){const lang=localStorage.getItem('mrjery_language')||'fr';return lang==='en'?r.en:lang==='ht'?r.ht:r.title;}
function mrjeryUpdateRankDisplays(){
 const wins=mrjeryGetWins(),r=mrjeryCurrentRank(wins),next=MRJERY_RANKS.find(x=>x.n===r.n+1),pct=next?Math.max(0,Math.min(100,(wins-r.wins)/(next.wins-r.wins)*100)):100;
 const lv=document.getElementById('dashboardLevel');if(lv)lv.innerHTML='Nivo '+r.n+' · <span class="rank-pill" style="color:'+r.color+'">['+r.sig+'] '+mrjeryRankLabel(r)+'</span>';
 const un=document.getElementById('dashboardUsername');if(un){un.textContent=currentUsername||'Joueur';un.title='['+r.sig+'] '+mrjeryRankLabel(r);}
 const prof=document.getElementById('profileRankContent');
 const summary='<div class="rank-current"><div class="rank-emblem" style="color:'+r.color+'">'+r.n+'</div><div><div class="rank-pill" style="color:'+r.color+'">['+r.sig+'] '+mrjeryRankLabel(r)+'</div><h3 style="margin:9px 0 4px">Niveau '+r.n+' · '+wins+' victoire(s)</h3><div class="rank-small">'+(next?(next.wins-wins)+' victoire(s) avant '+mrjeryRankLabel(next)+' ['+next.sig+']':'Tu as atteint le rang maximum !')+'</div><div class="rank-progress"><span style="width:'+pct+'%;background:'+r.color+'"></span></div><div class="rank-small">'+(next?wins+' / '+next.wins+' victoires':'Niveau maximum')+'</div></div></div>';
 if(prof)prof.innerHTML=summary;
 const cur=document.getElementById('rankingCurrent');if(cur)cur.innerHTML=summary;
 const tbody=document.getElementById('rankTableBody');if(tbody)tbody.innerHTML=MRJERY_RANKS.map(x=>'<tr class="'+(x.n===r.n?'current-rank':'')+'"><td>'+x.n+'</td><td><span class="rank-pill" style="color:'+x.color+'">['+x.sig+'] '+mrjeryRankLabel(x)+'</span></td><td>'+x.wins.toLocaleString()+'</td><td>'+(wins>=x.wins?'✅ Acquis':'🔒')+'</td></tr>').join('');
}
function openRankingScreen(){mrjeryUpdateRankDisplays();showScreen('rankingScreen');}
document.getElementById('openRanksFromProfile')?.addEventListener('click',openRankingScreen);
document.getElementById('rankingBack')?.addEventListener('click',()=>showScreen('accountMenuScreen'));

function mrjeryRenderPlayersDirectory(list){
  const body=document.getElementById('playersDirectoryBody');
  const status=document.getElementById('playersDirectoryStatus');
  if(!body)return;
  const players=Array.isArray(list)?list:[];
  body.innerHTML='';
  if(!players.length){body.innerHTML='<tr><td colspan="6">Pa gen kont jwè ki retounen nan baz done a.</td></tr>';if(status)status.textContent='0 jwè jwenn nan baz done a.';return;}
  players.sort((a,b)=>(Number(b.wins)||0)-(Number(a.wins)||0)||(Number(b.points)||0)-(Number(a.points)||0)||String(a.username||'').localeCompare(String(b.username||'')));
  players.forEach((player,index)=>{
    const wins=Math.max(0,Number(player.wins)||0);
    const rank=(()=>{let r=MRJERY_RANKS[0];for(const x of MRJERY_RANKS){if(wins>=x.wins)r=x;else break;}return r;})();
    const tr=document.createElement('tr');
    const tdPosition=document.createElement('td');tdPosition.textContent=String(index+1);
    const tdName=document.createElement('td');tdName.textContent=String(player.username||('Jwè '+(player.player_id??'')));
    const tdRank=document.createElement('td');tdRank.innerHTML='<span class="rank-pill" style="color:'+rank.color+'">['+rank.sig+'] '+mrjeryRankLabel(rank)+'</span>';
    const tdWins=document.createElement('td');tdWins.textContent=String(wins);
    const tdLosses=document.createElement('td');tdLosses.textContent=String(Math.max(0,Number(player.losses)||0));
    const tdState=document.createElement('td');tdState.textContent=player.in_game?'🎮 Nan yon pati':(player.online?'🟢 Anliy':'⚪ Offline');
    tr.append(tdPosition,tdName,tdRank,tdWins,tdLosses,tdState);body.appendChild(tr);
  });
  if(status)status.textContent=players.length+' kont enskri nan baz done a — lis la gen jwè online ak offline. Klasman an klase selon viktwa verifye.';
}
function mrjeryOpenPlayersDirectory(){
  showScreen('playersDirectoryScreen');
  const ranks=document.getElementById('playersDirectoryRanks');
  if(ranks && typeof MRJERY_RANKS!=='undefined') ranks.innerHTML=MRJERY_RANKS.map(x=>'<tr><td>'+x.n+'</td><td><span class="rank-pill" style="color:'+x.color+'">['+x.sig+'] '+mrjeryRankLabel(x)+'</span></td><td>'+x.wins.toLocaleString()+'</td></tr>').join('');
  const status=document.getElementById('playersDirectoryStatus');
  if(socket && socket.readyState===WebSocket.OPEN){if(status)status.textContent='Ap chaje tout kont jwè yo nan baz done a…';socket.send(JSON.stringify({type:'registered_players'}));}
  else if(status)status.textContent='Sèvè a pa konekte. Verifye koneksyon ak sèvè a, epi peze Rafrechi.';
}
document.getElementById('dashboardPlayersBtn')?.addEventListener('click',mrjeryOpenPlayersDirectory);
document.getElementById('dashboardPlayersCard')?.addEventListener('click',mrjeryOpenPlayersDirectory);
document.getElementById('playersDirectoryRefresh')?.addEventListener('click',()=>{const status=document.getElementById('playersDirectoryStatus');if(socket&&socket.readyState===WebSocket.OPEN){if(status)status.textContent='Ap rafrechi lis tout kont yo…';socket.send(JSON.stringify({type:'registered_players'}));}else if(status)status.textContent='Sèvè a pa konekte. Eseye ankò.';});
document.getElementById('playersDirectoryShowRanks')?.addEventListener('click',()=>openRankingScreen());
document.getElementById('playersDirectoryBack')?.addEventListener('click',()=>showScreen('accountMenuScreen'));


function showWinScreen(message) {

    stopAllTimers();
    // Les écrans de victoire de ce jeu signalent une victoire du joueur local.
    try { const key=mrjeryRankStorageKey(), data=JSON.parse(localStorage.getItem(key)||'{"wins":0}'); data.wins=Math.max(0,Number(data.wins)||0)+1; localStorage.setItem(key,JSON.stringify(data)); mrjeryUpdateRankDisplays(); } catch(e) { console.warn('Impossible de sauvegarder le rang local',e); }

    const result =
        document.getElementById(
            "winMessage"
        );

    if (result) {

        result.textContent =
            message;
    }

    showScreen(
        "winScreen"
    );
}

/* ==================================================
   BOUTONS ÉCRAN VICTOIRE
================================================== */

document
    .getElementById("winRestart")
    .addEventListener(
        "click",
        function() {

            const message =
                document
                    .getElementById(
                        "winMessage"
                    )
                    .textContent
                    .toLowerCase();

            if (
                message.includes("robot") ||
                message.includes("tu as gagné") ||
                message.includes("ton temps")
            ) {

                resetRobotGame();

                showScreen(
                    "robotScreen"
                );

            } else {

                resetLocalGame();

                showScreen(
                    "localScreen"
                );
            }
        }
    );

document
    .getElementById("winMenu")
    .addEventListener(
        "click",
        function() {

            stopAllTimers();

            // Après une partie contre le robot, revenir au tableau de bord
            // qui contient Paryaj, Defi et Jwe Anliy.
            showAccountMenu();
        }
    );

/* ==================================================
   MENU
================================================== */

document
    .getElementById("robotMode")
    .addEventListener(
        "click",
        function() {

            stopAllTimers();
            resetRobotGame();
            showScreen("robotScreen");
        }
    );

document
    .getElementById("localMode")
    .addEventListener(
        "click",
        function() {

            resetLocalGame();

            showScreen(
                "localScreen"
            );
        }
    );

document
    .getElementById("onlineMode")
    .addEventListener(
        "click",
        function() {

            document
                .getElementById(
                    "onlineError"
                )
                .textContent = "";

            document
                .getElementById(
                    "friendBox"
                )
                .classList.remove(
                    "show"
                );

            document
                .getElementById(
                    "searchingBox"
                )
                .classList.remove(
                    "show"
                );

            showScreen(
                "onlineScreen"
            );

            connectServer(function() { requestOnlinePlayers(); });
        }
    );

/* ==================================================
   ROBOT / LOCAL ACTIONS
================================================== */

document
    .getElementById("robotRestart")
    .addEventListener(
        "click",
        resetRobotGame
    );

document
    .getElementById("localRestart")
    .addEventListener(
        "click",
        resetLocalGame
    );

document
    .getElementById("robotUndo")
    .addEventListener(
        "click",
        undoRobot
    );

document
    .getElementById("localUndo")
    .addEventListener(
        "click",
        undoLocal
    );

document
    .getElementById("robotBack")
    .addEventListener(
        "click",
        function() {

            stopAllTimers();

            // Toujours revenir au tableau de bord avec Paryaj, Defi et Jwe Anliy,
            // même si la session n'est pas connectée.
            showAccountMenu();
        }
    );

document
    .getElementById("localBack")
    .addEventListener(
        "click",
        function() {

            stopAllTimers();

            showScreen(
                "homeScreen"
            );
        }
    );

/* ==================================================
   COMPTE - ACTIONS
================================================== */

document.getElementById("accountMode").addEventListener("click", function() {
    if (accountConnected) {
        showAccountMenu();
        return;
    }
    updateAccountDisplay();
    showAccountMessage("", true);
    showScreen("accountScreen");
    if (typeof setAuthMode === "function") setAuthMode("login");
});

document.getElementById("accountBack").addEventListener("click", function() {
    showScreen("localScreen");
});

document.getElementById("registerBtn").addEventListener("click", function() {
    const username = document.getElementById("registerUsername").value.trim();
    const email = document.getElementById("registerEmail").value.trim();
    const password = document.getElementById("registerPassword").value;
    const confirmation = document.getElementById("registerPasswordConfirmation").value;

    if (!username || !email || !password || !confirmation) {
        showAccountMessage("⚠️ Remplissez tous les champs.", false);
        return;
    }
    if (password !== confirmation) {
        showAccountMessage("⚠️ Les mots de passe ne correspondent pas.", false);
        return;
    }

    accountRequestInProgress = true;
    showAccountMessage("⏳ Création du compte...", true);

    connectServer(function() {
        if (!socket || socket.readyState !== WebSocket.OPEN) {
            accountRequestInProgress = false;
            showAccountMessage("❌ Serveur non disponible.", false);
            return;
        }
        socket.send(JSON.stringify({
            type: "register",
            username: username,
            email: email,
            password: password,
            password_confirmation: confirmation
        }));
    });
});

document.getElementById("loginBtn").addEventListener("click", function() {
    const login = document.getElementById("loginInput").value.trim();
    const password = document.getElementById("loginPassword").value;

    if (!login || !password) {
        showAccountMessage("⚠️ Entrez votre pseudo/email et votre mot de passe.", false);
        return;
    }

    accountRequestInProgress = true;
    showAccountMessage("⏳ Connexion...", true);

    connectServer(function() {
        if (!socket || socket.readyState !== WebSocket.OPEN) {
            accountRequestInProgress = false;
            showAccountMessage("❌ Serveur non disponible.", false);
            return;
        }
        socket.send(JSON.stringify({
            type: "login",
            login: login,
            password: password
        }));
    });
});

document.getElementById("accountPlayBtn").addEventListener("click", function() {
    // Accueil du compte : garder le tableau de bord avec Jwe Anliy, ami, Defi, Paryaj, etc.
    showScreen("accountMenuScreen");
});

document.getElementById("profileBtn").addEventListener("click", function() {
    document.getElementById("profileUsername").textContent = currentUsername || "---";
    document.getElementById("profileEmail").textContent = currentEmail || "---";
    document.getElementById("profilePlayerId").textContent = currentPlayerId || "---";
    mrjeryUpdateRankDisplays();
    showScreen("profileScreen");
});

document.getElementById("accountOnlineBtn").addEventListener("click", function() {
    onlineOpenedFromAccountMenu = true;
    const err = document.getElementById("onlineError");
    const status = document.getElementById("onlinePlayersStatus");
    const list = document.getElementById("onlinePlayersList");
    if (err) err.textContent = "";
    if (list) list.innerHTML = "";
    if (status) status.textContent = "Connexion au serveur de jeu…";
    document.getElementById("friendBox").classList.remove("show");
    document.getElementById("searchingBox").classList.remove("show");
    showScreen("onlineScreen");

    function loadPlayersAfterConnection() {
        if (!accountConnected) {
            if (status) status.textContent = "Connecte-toi pour voir les joueurs en ligne.";
            openAuth("login");
            showAccountMessage("Connecte-toi pour jouer en ligne.", false);
            return;
        }
        if (err) err.textContent = "";
        requestOnlinePlayers();
    }

    // Réutiliser la connexion si elle est vraiment ouverte; sinon créer une nouvelle.
    if (socket && socket.readyState === WebSocket.OPEN && !restoringAccountSession) {
        loadPlayersAfterConnection();
    } else {
        connectServer(loadPlayersAfterConnection);
        // Si le serveur Render se réveille lentement, ne pas laisser l'écran sans indication.
        setTimeout(function() {
            if (!document.getElementById("onlineScreen")?.classList.contains("active")) return;
            if (socket && socket.readyState === WebSocket.OPEN && !restoringAccountSession) return;
            if (status) status.textContent = "Le serveur met du temps à répondre. Attends un peu puis clique sur Jwe Anliy à nouveau.";
        }, 20000);
    }
});

document.getElementById("settingsBtn")?.addEventListener("click", function() {
    showScreen("settingsScreen");
});

document.getElementById("logoutBtn").addEventListener("click", function(event) {
    // Déconnexion explicite : effacer la session locale et afficher UNIQUEMENT Connexion.
    if (event) { event.preventDefault(); event.stopPropagation(); }
    const tokenToRevoke = accountToken;
    try {
        if (socket && socket.readyState === WebSocket.OPEN && tokenToRevoke) {
            socket.send(JSON.stringify({type:"logout_session", account_token:tokenToRevoke}));
        }
    } catch(e) {}
    try {
        localStorage.removeItem("mrjery_account_token");
        localStorage.removeItem("accountToken");
        sessionStorage.removeItem("mrjery_account_token");
        sessionStorage.removeItem("accountToken");
    } catch(e) {}
    try { closeOnlineConnection(); } catch(e) {}
    accountConnected = false;
    currentPlayerId = null;
    currentUsername = null;
    currentEmail = null;
    accountToken = null;
    accountRequestInProgress = false;

    ["registerUsername","registerEmail","registerPassword","registerPasswordConfirmation","loginInput","loginPassword"].forEach(function(id) {
        const field = document.getElementById(id);
        if (field) field.value = "";
    });
    try { updateAccountDisplay(); } catch(e) {}
    try { setAuthMode("login"); } catch(e) {}
    // Force the auth screen as the sole visible page; don't show the dashboard or landing page.
    showScreen("accountScreen");
    const authTitle = document.getElementById("authTitle");
    if (authTitle) authTitle.textContent = "Connexion";
    const loginPanel = document.getElementById("loginPanel");
    if (loginPanel) loginPanel.style.display = "block";
    const registerPanel = document.getElementById("registerPanel");
    if (registerPanel) registerPanel.style.display = "none";
    window.scrollTo(0, 0);
});

document.getElementById("accountMenuBack")?.addEventListener("click", function() {
    showScreen("localScreen");
});

document.getElementById("profileBack").addEventListener("click", function() {
    showAccountMenu();
});

document.getElementById("settingsBack").addEventListener("click", function() {
    showAccountMenu();
});


/* ==================================================
   ONLINE VARIABLES
================================================== */

let socket = null;

let onlinePlayer = null;
let onlineRoom = null;

let onlineBoardState = {};
let onlinePlayersState = {};

let onlineTurn = 1;

let onlineWinner = null;
let onlineGameOver = false;
let onlineDraw = false;
let onlineAbandonment = false;

let onlineBlackTime = START_TIME;
let onlineRedTime = START_TIME;

let onlineBlackScore = 0;
let onlineRedScore = 0;

let onlineGameNumber = 1;

let onlineStarter = 1;

let onlineWinningLine = null;

let onlineLastMove = null;
let onlineRematchRequest = null;
let onlineUndoRequest = null;

let onlineSessionToken = null;

let onlineConnectionMode = null;

let reconnectTimer = null;
let reconnectAttempts = 0;
let reconnecting = false;

let onlineDisplayInterval = null;
let onlinePlayersList = [];
let pendingGameInviteId = null;
let matchMicStream = null;
let matchVoicePeers = new Map();
let voicePeerMeta = new Map();
let voiceMutedPeers = new Set();
let voiceMuteAllSpectators = false;
let voiceJoinedRoom = null;
let matchMicEnabled = false;
let renderedChatSignature = "";

/* ==================================================
   JOUEURS EN LIGNE + INVITATION DIRECTE
================================================== */

function renderOnlinePlayers(list) {
    const container=document.getElementById("onlinePlayersList"), status=document.getElementById("onlinePlayersStatus");
    if(!container) { onlinePlayersList=Array.isArray(list)?list:[]; if(typeof mrjeryRenderPlayersDirectory==='function')mrjeryRenderPlayersDirectory(onlinePlayersList); return; } container.innerHTML=""; onlinePlayersList=Array.isArray(list)?list:[]; if(typeof mrjeryRenderPlayersDirectory==='function')mrjeryRenderPlayersDirectory(onlinePlayersList);
    if(!onlinePlayersList.length){if(status)status.textContent="Aucun autre joueur en ligne pour le moment.";return;}
    if(status)status.textContent=onlinePlayersList.length+" joueur(s) en ligne.";
    onlinePlayersList.forEach(function(player){
        const row=document.createElement("div"); row.className="online-player-row";
        const name=document.createElement("div"); name.className="online-player-name"; name.textContent="🟢 "+(player.username||player.name||"Joueur");
        const state=document.createElement("span"); state.className="online-player-state"; state.textContent=player.in_game?"En partie":"Disponible"; name.appendChild(state);
        const btn=document.createElement("button"); btn.type="button"; btn.className="online-player-invite"; btn.textContent="🎮 Envoyer un match"; btn.disabled=Boolean(player.in_game)||!accountConnected;
        btn.addEventListener("click",function(){sendGameInvite(Number(player.player_id));}); row.appendChild(name); row.appendChild(btn); container.appendChild(row);
    });
}
function requestOnlinePlayers(){
    const status=document.getElementById("onlinePlayersStatus");
    const err=document.getElementById("onlineError");
    if(!accountConnected){
        if(status) status.textContent="Connecte-toi pour voir les joueurs en ligne.";
        return;
    }
    if(socket && socket.readyState===WebSocket.OPEN && !restoringAccountSession){
        if(status) status.textContent="Recherche des joueurs en ligne…";
        try { socket.send(JSON.stringify({type:"online_players"})); }
        catch(e){ if(status) status.textContent="Impossible d’interroger le serveur. Réessaie."; }
        return;
    }
    if(status) status.textContent="Connexion au serveur de jeu…";
    if(err) err.textContent="Le serveur est en cours de connexion. La liste se chargera dès que la session sera rétablie.";
}
function showGameInvite(id,from,duration,size){
    pendingGameInviteId=id||null;
    const b=document.getElementById("gameInviteBox"),m=document.getElementById("gameInviteMessage");
    const message="🎮 "+(from||"Un joueur")+" vous invite à jouer — "+(duration||5)+" min · tableau "+(size||15)+"×"+(size||15)+".";
    if(b&&m){
        m.textContent=message;
        /* Garde la demande visible au-dessus de tous les écrans, sans changer le reste du site. */
        if(b.parentElement!==document.body) document.body.appendChild(b);
        b.style.setProperty("display","block","important");
        b.style.setProperty("visibility","visible","important");
        b.style.setProperty("opacity","1","important");
        b.style.setProperty("z-index","2147483647","important");
        b.setAttribute("aria-modal","true");
        try { if(document.hidden && "Notification" in window && Notification.permission==="granted") new Notification("MR_Jery Morpion",{body:message}); } catch(e) {}
        document.title="🎮 Invitation ! MR_Jery Morpion";
    }
}
function hideGameInvite(){pendingGameInviteId=null;const b=document.getElementById("gameInviteBox"),m=document.getElementById("gameInviteMessage");if(b){b.style.setProperty("display","none","important");b.removeAttribute("aria-modal");}if(m)m.textContent="";document.title=document.title.replace("🎮 Invitation ! ","");}
function sendGameInvite(id){if(!accountConnected)return;if(!socket||socket.readyState!==WebSocket.OPEN){document.getElementById("onlineError").textContent="Connexion au serveur en cours...";return;}const duration=Number(document.getElementById("inviteDuration")?.value||5);const boardSize=Number(document.getElementById("inviteBoardSize")?.value||15);socket.send(JSON.stringify({type:"invite_player",target_player_id:Number(id),duration_minutes:Math.max(1,Math.min(30,duration)),board_size:Math.max(13,Math.min(20,boardSize))}));}
function answerGameInvite(ok){if(!pendingGameInviteId||!socket||socket.readyState!==WebSocket.OPEN)return;socket.send(JSON.stringify({type:"invite_response",invitation_id:pendingGameInviteId,accepted:Boolean(ok)}));hideGameInvite();}
document.getElementById("acceptGameInviteBtn").addEventListener("click",function(){answerGameInvite(true);});
document.getElementById("refuseGameInviteBtn").addEventListener("click",function(){answerGameInvite(false);});

/* ==================================================
   MATCHMAKING
================================================== */

let searchingForOpponent = false;

/* ==================================================
   TROUVER ADVERSAIRE
================================================== */

document
    .getElementById("findOpponentBtn")
    .addEventListener(
        "click",
        function() {

            searchingForOpponent = true;

            document
                .getElementById(
                    "friendBox"
                )
                .classList.remove(
                    "show"
                );

            document
                .getElementById(
                    "searchingBox"
                )
                .classList.add(
                    "show"
                );

            document
                .getElementById(
                    "onlineError"
                )
                .textContent = "";

            onlineConnectionMode =
                "matchmaking";

            connectServer(
                function() {

                    if (
                        !socket ||
                        socket.readyState !==
                        WebSocket.OPEN
                    ) {
                        return;
                    }

                    socket.send(
                        JSON.stringify({
                            type:
                                "find_match"
                        })
                    );
                }
            );
        }
    );

/* ==================================================
   ANNULER RECHERCHE
================================================== */

document
    .getElementById("cancelSearchBtn")
    .addEventListener(
        "click",
        function() {

            searchingForOpponent =
                false;

            document
                .getElementById(
                    "searchingBox"
                )
                .classList.remove(
                    "show"
                );

            if (
                socket &&
                socket.readyState ===
                WebSocket.OPEN
            ) {

                socket.send(
                    JSON.stringify({
                        type:
                            "cancel_match"
                    })
                );
            }

            closeOnlineConnection();

        }
    );

/* ==================================================
   JOUER AVEC UN AMI
================================================== */

document
    .getElementById("friendModeBtn")
    .addEventListener(
        "click",
        function() {

            document
                .getElementById(
                    "searchingBox"
                )
                .classList.remove(
                    "show"
                );

            document
                .getElementById(
                    "friendBox"
                )
                .classList.add(
                    "show"
                );

            document
                .getElementById(
                    "onlineError"
                )
                .textContent = "";

        }
    );

/* ==================================================
   REGARDER UN MATCH
================================================== */

document
    .getElementById("spectatorModeBtn")
    .addEventListener(
        "click",
        function() {

            onlineConnectionMode = "spectator-list";
            onlinePlayer = 0;
            onlineRoom = null;
            onlineSessionToken = null;
            onlineBoardState = {};
            onlinePlayersState = {};
            onlineRematchRequest = null;
            onlineLastMove = null;

            const list = document.getElementById("liveMatchList");
            const error = document.getElementById("spectatorError");

            if (list) {
                list.innerHTML = '<div class="live-empty">🔎 Recherche des matchs en direct...</div>';
            }

            if (error) {
                error.textContent = "";
            }

            showScreen("spectatorScreen");

            connectServer(function() {

                if (socket && socket.readyState === WebSocket.OPEN) {
                    socket.send(JSON.stringify({
                        type: "live_matches"
                    }));
                }
            });
        }
    );

document
    .getElementById("spectatorBack")
    .addEventListener(
        "click",
        function() {
            closeOnlineConnection();
            showScreen("onlineScreen");
        }
    );

/* ==================================================
   SALLE D'ATTENTE
================================================== */

document.getElementById("waitingRoomBtn").addEventListener("click", function() {
    if (!accountConnected) {
        showScreen("accountScreen");
        showAccountMessage("🔐 Connectez-vous pour accéder à la salle d'attente.", false);
        return;
    }
    if (!onlineRoom) {
        document.getElementById("waitingStatus").textContent = "Aucune partie créée pour le moment.";
    } else {
        document.getElementById("waitingRoomCode").textContent = onlineRoom;
        document.getElementById("waitingStatus").textContent = "⏳ En attente du deuxième joueur...";
    }
    showScreen("waitingRoomScreen");
});

document.getElementById("waitingBack").addEventListener("click", function() {
    showScreen("onlineScreen");
});

document.getElementById("refreshSpectatorBtn").addEventListener("click", function() {
    if (onlineConnectionMode !== "spectator") {
        onlineConnectionMode = "spectator-list";
    }
    if (socket && socket.readyState === WebSocket.OPEN) {
        socket.send(JSON.stringify({type:"live_matches"}));
    } else {
        connectServer(function() {
            if (socket && socket.readyState === WebSocket.OPEN) {
                socket.send(JSON.stringify({type:"live_matches"}));
            }
        });
    }
});

/* ==================================================
   TIMER ONLINE
================================================== */

function updateOnlineTimers() {

    const blackTime =
        Math.max(
            0,
            Math.floor(
                Number(
                    onlineBlackTime
                ) || 0
            )
        );

    const redTime =
        Math.max(
            0,
            Math.floor(
                Number(
                    onlineRedTime
                ) || 0
            )
        );

    document
        .getElementById(
            "onlineBlackTime"
        )
        .textContent =
        formatTime(
            blackTime
        );

    document
        .getElementById(
            "onlineRedTime"
        )
        .textContent =
        formatTime(
            redTime
        );

    const blackBox =
        document.getElementById(
            "onlineBlackTimer"
        );

    const redBox =
        document.getElementById(
            "onlineRedTimer"
        );

    blackBox.classList.toggle(
        "active",
        onlineTurn === 1 &&
        !onlineGameOver &&
        onlineRematchRequest === null
    );

    redBox.classList.toggle(
        "active",
        onlineTurn === 2 &&
        !onlineGameOver &&
        onlineRematchRequest === null
    );

    blackBox.classList.toggle(
        "warning",
        blackTime <= 60
    );

    redBox.classList.toggle(
        "warning",
        redTime <= 60
    );
}

function startOnlineDisplayTimer() {

    stopOnlineDisplayTimer();

    onlineDisplayInterval =
        setInterval(
            function() {

                updateOnlineTimers();

            },
            500
        );

    updateOnlineTimers();
}

function stopOnlineDisplayTimer() {

    if (onlineDisplayInterval) {

        clearInterval(
            onlineDisplayInterval
        );

        onlineDisplayInterval = null;
    }
}

/* ==================================================
   CONVERSION TABLEAU SERVEUR
================================================== */

function convertServerBoard(board) {
    const converted = {};
    if (Array.isArray(board)) {
        for (let row=0; row<BOARD_SIZE; row++) {
            if (!Array.isArray(board[row])) continue;
            for (let col=0; col<BOARD_SIZE; col++) {
                const raw=board[row][col];
                const value=raw && typeof raw === "object" ? (raw.color || raw.player || raw.value || 0) : raw;
                if (Number(value)===1 || value==="black") converted[row+","+col]="black";
                else if (Number(value)===2 || value==="red") converted[row+","+col]="red";
            }
        }
        return converted;
    }
    if (board && typeof board === "object") {
        for (const key of Object.keys(board)) {
            const m=key.match(/^(\d+)[,;](\d+)$/); if(!m) continue;
            const row=Number(m[1]), col=Number(m[2]); if(row<0||row>=BOARD_SIZE||col<0||col>=BOARD_SIZE) continue;
            const raw=board[key]; const value=raw && typeof raw === "object" ? (raw.color || raw.player || raw.value || 0) : raw;
            if(Number(value)===1 || value==="black") converted[row+","+col]="black";
            else if(Number(value)===2 || value==="red") converted[row+","+col]="red";
        }
    }
    return converted;
}

/* ==================================================
   CONNECTER SERVEUR
================================================== */

function connectServer(callback) {

    if (
        socket &&
        socket.readyState ===
        WebSocket.OPEN
    ) {
        // Si la restauration est en cours, attendre l'identification du serveur.
        // Cela évite de lancer un jeu avant que le compte soit reconnu.
        if (restoringAccountSession) {
            if (callback) pendingRestoreCallback = callback;
            return;
        }
        if (callback) callback();
        return;
    }

    if (
        socket &&
        socket.readyState ===
        WebSocket.CONNECTING
    ) {
        // Important : ne pas perdre l'action (ex. charger les joueurs en ligne)
        // si l'utilisateur ouvre Jwe Anliy pendant l'ouverture du WebSocket.
        if (typeof callback === "function") pendingConnectionCallbacks.push(callback);
        return;
    }

    socket =
        new WebSocket(
            SERVER_URL
        );

    socket.onopen =
        function() {

            console.log(
                "Serveur connecté"
            );

            reconnectAttempts = 0;
            reconnecting = false;
            // Re-authentifier chaque nouvelle connexion WebSocket avec le jeton sauvegardé.
            // Le compte reste connecté après navigation, actualisation ou reconnexion réseau;
            // seule la déconnexion explicite retire le jeton local.
            let savedToken = null;
            try { savedToken = localStorage.getItem("mrjery_account_token"); } catch(e) {}
            if (savedToken && !accountRequestInProgress) {
                restoringAccountSession = true;
                pendingRestoreCallback = callback || null;
                if (restoreSessionTimeout) clearTimeout(restoreSessionTimeout);
                restoreSessionTimeout = setTimeout(function(){
                    if (!restoringAccountSession) return;
                    // Un délai réseau n'est PAS une déconnexion : conserver le jeton.
                    // Ne pas envoyer le joueur à Connexion tant que le serveur n'a pas
                    // répondu que le jeton est réellement invalide.
                    restoringAccountSession = false;
                    const err = document.getElementById("onlineError");
                    if (err) err.textContent = "Le serveur tarde à répondre. Ton compte reste mémorisé : vérifie la connexion puis réessaie, sans te reconnecter.";
                    const status = document.getElementById("onlineStatus");
                    if (status) status.textContent = "Session conservée — serveur en attente";
                    try {
                        const oldSocket = socket;
                        socket = null;
                        if (oldSocket && oldSocket.readyState < WebSocket.CLOSING) oldSocket.close();
                    } catch(e) {}
                }, 60000);
                socket.send(JSON.stringify({type:"restore_session", account_token:savedToken}));
            } else {
                if (callback) callback();
                runPendingConnectionCallbacks();
            }

            if (reconnectTimer) {

                clearTimeout(
                    reconnectTimer
                );

                reconnectTimer = null;
            }

            // Si on restaure une session, le callback sera exécuté après restore_session_result.
        };

    socket.onclose =
        function() {

            stopOnlineDisplayTimer();

            if (
                onlineRoom &&
                onlineSessionToken &&
                onlinePlayer
            ) {

                scheduleReconnect();

            } else {

                const status =
                    document.getElementById(
                        "onlineStatus"
                    );

                if (status) {

                    status.textContent =
                        "Serveur déconnecté";
                }
            }
        };

    socket.onerror =
        function() {

            const onlineError =
                document.getElementById(
                    "onlineError"
                );

            const gameError =
                document.getElementById(
                    "gameOnlineError"
                );

            if (onlineError) {

                onlineError.textContent =
                    "Erreur de connexion.";
            }

            if (gameError) {

                gameError.textContent =
                    "Erreur de connexion.";
            }
        };

    socket.onmessage =
        function(event) {

            try {

                const data =
                    JSON.parse(
                        event.data
                    );

                /* ==================================
                   COMPTE - INSCRIPTION
                ================================== */

                if (data.type === "register_result") {

                    accountRequestInProgress = false;

                    if (data.success) {
                        currentPlayerId = data.player_id || null;
                        currentUsername = data.username || null;
                        currentEmail = data.email || null;
                        accountToken = data.account_token || null;
                        accountConnected = true;
                        try { if(accountToken) localStorage.setItem("mrjery_account_token", accountToken); } catch(e) {}

                        updateAccountDisplay();
                        showAccountMessage(
                            "✅ " + (data.message || "Compte créé avec succès."),
                            true
                        );

                        setTimeout(function() {
                            showAccountMenu();
                        }, 500);
                    } else {
                        showAccountMessage(
                            "❌ " + (data.message || "Impossible de créer le compte."),
                            false
                        );
                    }

                    return;
                }

                /* ==================================
                   COMPTE - CONNEXION
                ================================== */

                if (data.type === "login_result") {

                    accountRequestInProgress = false;

                    if (data.success) {
                        currentPlayerId = data.player_id || null;
                        currentUsername = data.username || null;
                        currentEmail = data.email || null;
                        accountToken = data.account_token || null;
                        accountConnected = true;
                        try { if(accountToken) localStorage.setItem("mrjery_account_token", accountToken); } catch(e) {}

                        updateAccountDisplay();
                        showAccountMessage(
                            "✅ " + (data.message || "Connexion réussie."),
                            true
                        );

                        setTimeout(function() {
                            showAccountMenu();
                        }, 500);
                    } else {
                        showAccountMessage(
                            "❌ " + (data.message || "Pseudo/email ou mot de passe incorrect."),
                            false
                        );
                    }

                    return;
                }

                if (data.type === "restore_session_result") {
                    restoringAccountSession = false;
                    if (restoreSessionTimeout) { clearTimeout(restoreSessionTimeout); restoreSessionTimeout = null; }
                    if (data.success) {
                        currentPlayerId = data.player_id || null;
                        currentUsername = data.username || null;
                        currentEmail = data.email || null;
                        try { accountToken = data.account_token || localStorage.getItem("mrjery_account_token") || null; } catch(e) { accountToken = data.account_token || accountToken || null; }
                        accountConnected = Boolean(accountToken || currentPlayerId || currentUsername);
                        updateAccountDisplay();
                        refreshDashboardUser();
                    } else {
                        // Session non valide : demander une connexion explicite.
                        accountConnected = false;
                        accountToken = null;
                        try { localStorage.removeItem("mrjery_account_token"); } catch(e) {}
                        openAuth("login");
                        showAccountMessage("Ta session a expiré ou n'est plus valide. Connecte-toi à nouveau.", false);
                    }
                    const cb = pendingRestoreCallback;
                    pendingRestoreCallback = null;
                    if (typeof cb === "function") cb();
                    // Après la restauration de session, exécuter aussi les actions
                    // mises en attente pendant que le WebSocket s'ouvrait.
                    runPendingConnectionCallbacks();
                    return;
                }

                /* ==================================
                   JOUEURS EN LIGNE / INVITATIONS
                ================================== */

                if (data.type === "online_players") { renderOnlinePlayers(data.players || []); return; }
                if (data.type === "registered_players") { if(data.success){mrjeryRenderPlayersDirectory(data.players||[]);}else{const st=document.getElementById("playersDirectoryStatus");if(st)st.textContent=data.message||"Pa t kapab chaje lis tout jwè yo.";} return; }
                if (data.type === "game_invite") { showGameInvite(data.invitation_id, data.from_username, data.duration_minutes, data.board_size); return; }
                if (data.type === "voice_peer_join") { handleVoicePeerJoin(data); return; }
                if (data.type === "voice_peer_left") { const id=String(data.peer_id); closeVoicePeer(id); voicePeerMeta.delete(id); document.getElementById('voiceAudio_'+id)?.remove(); renderVoicePeerControls(); return; }
                if (data.type === "voice_peer_list") { handleVoicePeerList(data.peers || []); return; }
                if (data.type === "voice_signal") { handleVoiceSignal(data); return; }
                if (data.type === "invite_result") { const b=document.getElementById("onlineError"); if(b)b.textContent=data.message||""; return; }
                if (data.type === "direct_match") {
                    onlineRoom=data.room; onlinePlayer=Number(data.player); onlineSessionToken=data.session_token||null; onlineConnectionMode="direct_invite"; onlineLastMove=null; onlineRematchRequest=null; onlineUndoRequest=null;
                    const n=document.getElementById("onlineMatchNotice"); if(n){n.textContent=data.message||"🎮 Match accepté ! La partie va commencer.";setTimeout(function(){n.textContent="";},5000);}
                    document.getElementById("roomCode").textContent="Match direct"; document.getElementById("playerNumber").textContent=onlinePlayer; document.getElementById("gameRoomCode").textContent="Direct"; document.getElementById("onlineError").textContent="";
                    showScreen("onlineGameScreen"); createBoard(document.getElementById("onlineBoard"),onlineClick); startOnlineDisplayTimer(); return;
                }

                /* ==================================
                   RECHERCHE
                ================================== */

                if (
                    data.type ===
                    "searching"
                ) {

                    searchingForOpponent =
                        true;

                    document
                        .getElementById(
                            "searchingBox"
                        )
                        .classList.add(
                            "show"
                        );

                    document
                        .getElementById(
                            "onlineError"
                        )
                        .textContent = "";

                    return;
                }

                /* ==================================
                   LISTE DES MATCHS EN DIRECT
                ================================== */

                if (data.type === "live_matches") {

                    const list = document.getElementById("liveMatchList");

                    if (!list) {
                        return;
                    }

                    list.innerHTML = "";

                    const matches = Array.isArray(data.matches)
                        ? data.matches
                        : [];

                    if (matches.length === 0) {
                        list.innerHTML =
                            '<div class="live-empty">👁️ Aucun match en direct pour le moment.</div>';
                        return;
                    }

                    matches.forEach(function(match) {

                        const button = document.createElement("button");
                        button.type = "button";
                        button.className = "live-match-button";
                        button.textContent =
                            "👁️ " +
                            (match.player1 || "Joueur 1") +
                            " ⚫ VS 🔴 " +
                            (match.player2 || "Joueur 2") +
                            "   •   Spectateurs : " +
                            Number(match.spectator_count || 0);

                        button.addEventListener("click", function() {

                            onlineConnectionMode = "spectator";
                            onlinePlayer = 0;
                            onlineRoom = match.room;
                            onlineSessionToken = null;

                            if (socket && socket.readyState === WebSocket.OPEN) {
                                socket.send(JSON.stringify({
                                    type: "watch",
                                    room: match.room
                                }));
                            }
                        });

                        list.appendChild(button);
                    });

                    return;
                }

                /* ==================================
                   MATCH TROUVÉ
                ================================== */

                if (
                    data.type ===
                    "match_found"
                ) {

                    searchingForOpponent =
                        false;

                    onlineRoom =
                        data.room;

                    onlinePlayer =
                        Number(
                            data.player
                        );

                    onlineSessionToken =
                        data.session_token ||
                        null;

                    onlineConnectionMode =
                        "matchmaking";

                    const matchNotice = document.getElementById("onlineMatchNotice");
                    if (matchNotice) {
                        matchNotice.textContent =
                            data.message || "🎮 Adversaire trouvé ! Le match va commencer.";
                        setTimeout(function() {
                            if (matchNotice) {
                                matchNotice.textContent = "";
                            }
                        }, 5000);
                    }

                    onlineLastMove = null;
                    onlineRematchRequest =
                        null;
                    onlineUndoRequest = null;

                    document
                        .getElementById(
                            "searchingBox"
                        )
                        .classList.remove(
                            "show"
                        );

                    document
                        .getElementById(
                            "friendBox"
                        )
                        .classList.remove(
                            "show"
                        );

                    document
                        .getElementById(
                            "roomCode"
                        )
                        .textContent =
                        "Match automatique";

                    document
                        .getElementById(
                            "playerNumber"
                        )
                        .textContent =
                        onlinePlayer;

                    document
                        .getElementById(
                            "gameRoomCode"
                        )
                        .textContent =
                        "Automatique";

                    document
                        .getElementById(
                            "onlineError"
                        )
                        .textContent = "";

                    showScreen(
                        "onlineGameScreen"
                    );

                    createBoard(
                        document.getElementById(
                            "onlineBoard"
                        ),
                        onlineClick
                    );

                    startOnlineDisplayTimer();

                    return;
                }

                /* ==================================
                   PARTIE CRÉÉE
                ================================== */

                if (
                    data.type ===
                    "created"
                ) {

                    onlineRoom =
                        data.room;

                    onlinePlayer =
                        Number(
                            data.player
                        );

                    onlineSessionToken =
                        data.session_token ||
                        null;

                    onlineConnectionMode =
                        "create";

                    onlineLastMove = null;
                    onlineRematchRequest =
                        null;

                    document
                        .getElementById(
                            "roomCode"
                        )
                        .textContent =
                        onlineRoom;

                    document
                        .getElementById(
                            "playerNumber"
                        )
                        .textContent =
                        onlinePlayer;

                    document
                        .getElementById(
                            "gameRoomCode"
                        )
                        .textContent =
                        onlineRoom;

                    const playerRoomRow = document.getElementById("gameRoomCode");
                    if (playerRoomRow && playerRoomRow.parentElement) playerRoomRow.parentElement.style.display = "block";

                    document
                        .getElementById(
                            "onlineError"
                        )
                        .textContent = "";

                    showScreen(
                        "onlineGameScreen"
                    );

                    createBoard(
                        document.getElementById(
                            "onlineBoard"
                        ),
                        onlineClick
                    );

                    startOnlineDisplayTimer();

                    return;
                }

                /* ==================================
                   JOIN
                ================================== */

                if (
                    data.type ===
                    "joined"
                ) {

                    onlineRoom =
                        data.room;

                    onlinePlayer =
                        Number(
                            data.player
                        );

                    onlineSessionToken =
                        data.session_token ||
                        null;

                    onlineConnectionMode =
                        "join";

                    onlineLastMove = null;
                    onlineRematchRequest =
                        null;

                    document
                        .getElementById(
                            "roomCode"
                        )
                        .textContent =
                        onlineRoom;

                    document
                        .getElementById(
                            "playerNumber"
                        )
                        .textContent =
                        onlinePlayer;

                    document
                        .getElementById(
                            "gameRoomCode"
                        )
                        .textContent =
                        onlineRoom;

                    document
                        .getElementById(
                            "onlineError"
                        )
                        .textContent = "";

                    showScreen(
                        "onlineGameScreen"
                    );

                    createBoard(
                        document.getElementById(
                            "onlineBoard"
                        ),
                        onlineClick
                    );

                    startOnlineDisplayTimer();

                    return;
                }

                /* ==================================
                   SPECTATEUR CONNECTÉ
                ================================== */

                if (data.type === "watching") {

                    onlineConnectionMode = "spectator";
                    onlinePlayer = 0;
                    onlineRoom = data.room;
                    onlineSessionToken = null;

                    document.getElementById("gameRoomCode").textContent = data.room;
                    const spectatorRoom = document.getElementById("gameRoomCode");
                    if (spectatorRoom && spectatorRoom.parentElement) spectatorRoom.parentElement.style.display = "none";
                    document.getElementById("gameOnlineError").textContent = "";

                    showScreen("onlineGameScreen");

                    createBoard(
                        document.getElementById("onlineBoard"),
                        onlineClick
                    );

                    startOnlineDisplayTimer();
                    return;
                }

                /* ==================================
                   RECONNECT
                ================================== */

                if (
                    data.type ===
                    "reconnected"
                ) {

                    onlineRoom =
                        data.room;

                    onlinePlayer =
                        Number(
                            data.player
                        );

                    onlineSessionToken =
                        data.session_token ||
                        onlineSessionToken;

                    document
                        .getElementById(
                            "gameRoomCode"
                        )
                        .textContent =
                        onlineRoom;

                    showScreen(
                        "onlineGameScreen"
                    );

                    createBoard(
                        document.getElementById(
                            "onlineBoard"
                        ),
                        onlineClick
                    );

                    startOnlineDisplayTimer();

                    return;
                }

                /* ==================================
                   ÉTAT DU JEU
                ================================== */

                if (
                    data.type ===
                    "state"
                ) {

                    onlineBoardState =
                        convertServerBoard(
                            data.board
                        );
                    onlineLastMove = data.last_move || null;

                    onlinePlayersState =
                        data.players || {};
                    if (Array.isArray(onlinePlayersState)) {
                        const normalizedPlayers = {};
                        onlinePlayersState.forEach(function(player){ if(player && player.player) normalizedPlayers[String(player.player)]=player; });
                        onlinePlayersState=normalizedPlayers;
                    }
                    renderMatchChat(data.chat || []);
                    ensureVoiceJoined();

                    const spectatorCount = document.getElementById("onlineSpectatorCount");
                    if (spectatorCount) {
                        spectatorCount.textContent =
                            "👁️ Spectateurs : " + Number(data.spectator_count || data.spectators_count || 0);
                    }

                    onlineTurn =
                        Number(
                            data.turn || 1
                        );

                    onlineStarter =
                        Number(
                            data.starter || 1
                        );

                    onlineWinner =
                        data.winner
                            ? Number(
                                data.winner
                            )
                            : null;

                    onlineGameOver =
                        Boolean(
                            data.game_over
                        );

                    onlineDraw =
                        Boolean(
                            data.draw
                        );

                    onlineAbandonment =
                        Boolean(
                            data.abandonment
                        );

                    onlineBlackTime = Number.isFinite(Number(data.black_time)) ? Number(data.black_time) : START_TIME;

                    onlineRedTime = Number.isFinite(Number(data.red_time)) ? Number(data.red_time) : START_TIME;

                    onlineBlackScore =
                        Number(
                            data.black_score || 0
                        );

                    onlineRedScore =
                        Number(
                            data.red_score || 0
                        );

                    onlineGameNumber =
                        Number(
                            data.game_number || 1
                        );

                    onlineLastMove =
                        data.last_move ||
                        null;
                    const incomingSize = Array.isArray(data.board) && data.board.length ? data.board.length : BOARD_SIZE;
                    if (incomingSize >= 13 && incomingSize <= 20 && incomingSize !== BOARD_SIZE) {
                        BOARD_SIZE = incomingSize;
                        const liveBoard = document.getElementById("onlineBoard");
                        if (liveBoard) createBoard(liveBoard, onlineClick);
                    }

                    /*
                       IMPORTANT:
                       Le serveur envoie ici
                       directement 1 ou 2.
                    */

                    onlineRematchRequest =
                        data.rematch_request !==
                        undefined &&
                        data.rematch_request !==
                        null
                            ? Number(
                                data.rematch_request
                            )
                            : null;

                    onlineUndoRequest =
                        data.undo_request !==
                        undefined &&
                        data.undo_request !==
                        null
                            ? Number(data.undo_request)
                            : null;

                    onlineWinningLine =
                        data.winning_line ||
                        null;

                    renderOnlineState();

                    updateOnlineScoreDisplay();
                    updateOnlineStatus();
                    updateOnlineResult();
                    updateOnlineTimers();
                    updateRematchUI();
                    updateUndoUI();
                    updateOnlineNewGameButton();

                    startOnlineDisplayTimer();

                    return;
                }

                /* ==================================
                   ERROR
                ================================== */

                if (
                    data.type ===
                    "error"
                ) {

                    const message =
                        data.message ||
                        "Erreur.";

                    const onlineError =
                        document.getElementById(
                            "onlineError"
                        );

                    const gameError =
                        document.getElementById(
                            "gameOnlineError"
                        );

                    if (onlineError) {

                        onlineError.textContent =
                            message;
                    }

                    if (gameError) {

                        gameError.textContent =
                            message;
                    }

                    return;
                }

            } catch(error) {

                console.error(
                    "Erreur message serveur:",
                    error
                );
            }
        };
}

/* ==================================================
   SCORE
================================================== */

function updateOnlineScoreDisplay() {

    const p1 = onlinePlayersState["1"] || {};
    const p2 = onlinePlayersState["2"] || {};

    const blackName = document.getElementById("onlineBlackName");
    const redName = document.getElementById("onlineRedName");

    if (blackName) {
        blackName.textContent = p1.username || p1.name || "Joueur 1";
    }

    if (redName) {
        redName.textContent = p2.username || p2.name || "Joueur 2";
    }

    const blackTimerLabel = document.querySelector("#onlineBlackTimer .timer-label");
    const redTimerLabel = document.querySelector("#onlineRedTimer .timer-label");
    if (blackTimerLabel) blackTimerLabel.textContent = "⚫ " + (p1.name || p1.username || "Joueur 1");
    if (redTimerLabel) redTimerLabel.textContent = "🔴 " + (p2.name || p2.username || "Joueur 2");

    document
        .getElementById(
            "onlineBlackScore"
        )
        .textContent =
        onlineBlackScore;

    document
        .getElementById(
            "onlineRedScore"
        )
        .textContent =
        onlineRedScore;
}

/* ==================================================
   STATUS ONLINE CORRIGÉ
================================================== */

function updateOnlineStatus() {

    const status =
        document.getElementById(
            "onlineStatus"
        );

    if (!status) {
        return;
    }
    status.classList.remove("opponent-turn");

    if (onlineConnectionMode === "spectator") {
        if (onlineGameOver) {
            status.textContent = onlineDraw
                ? "🤝 Match nul"
                : "👁️ Match terminé";
        } else {
            status.textContent = "👁️ Vous regardez le match en direct";
        }
        return;
    }

    /*
       DEMANDE REJWE
    */

    if (onlineUndoRequest !== null) {
        document.getElementById("gameOnlineError").textContent =
            "⏳ Attendez la réponse au rejwe.";
        return;
    }

    if (
        onlineRematchRequest !== null
    ) {

        const requester =
            Number(
                onlineRematchRequest
            );

        if (
            requester ===
            Number(onlinePlayer)
        ) {

            status.textContent =
                "⏳ Demande rejwe en attente...";

        } else {

            status.textContent =
                "🔄 L'adversaire demande un rejwe.";
        }

        return;
    }

    /*
       MATCH FINI
    */

    if (onlineGameOver) {

        if (onlineAbandonment) {
            status.textContent =
                Number(onlineWinner) === Number(onlinePlayer)
                    ? "🚪 Votre adversaire a quitté la partie. Vous gagnez par abandon."
                    : "❌ Partie terminée par abandon.";
            return;
        }

        if (onlineDraw) {

            status.textContent =
                "🤝 Match nul";

        } else if (
            Number(onlineWinner) ===
            Number(onlinePlayer)
        ) {

            status.textContent =
                "🏆 OU GENYEN";

        } else {

            status.textContent =
                "❌ OU PÈDI";
        }

        return;
    }

    const player1 =
        onlinePlayersState["1"];

    const player2 =
        onlinePlayersState["2"];

    if (
        onlinePlayer === 1 &&
        player2 &&
        !player2.connected
    ) {

        status.textContent =
            "En attente du deuxième joueur...";

        return;
    }

    if (
        onlinePlayer === 2 &&
        player1 &&
        !player1.connected
    ) {

        status.textContent =
            "En attente du premier joueur...";

        return;
    }

    if (
        Number(onlinePlayer) ===
        Number(onlineTurn)
    ) {

        status.textContent =
            "À ton tour";

    } else {

        status.textContent =
            "ADVERSAIRE À JOUER";
        status.classList.add("opponent-turn");
    }
}

/* ==================================================
   RESULTAT ONLINE CORRIGÉ
================================================== */

function updateOnlineResult() {

    const result =
        document.getElementById(
            "onlineResult"
        );

    if (!result) {
        return;
    }

    if (!onlineGameOver) {

        result.textContent = "";

        result.classList.remove(
            "show"
        );

        return;
    }

    result.classList.add(
        "show"
    );

    if (onlineDraw) {

        result.textContent =
            "🤝 MATCH NUL";

        return;
    }

    if (onlineConnectionMode === "spectator") {
        const winnerName = onlinePlayersState[String(onlineWinner)]?.name ||
            onlinePlayersState[String(onlineWinner)]?.username ||
            "Le joueur gagnant";

        result.textContent = onlineAbandonment
            ? "🚪 Match terminé : " + winnerName + " gagne par abandon."
            : "🏆 Gagnant : " + winnerName;
        return;
    }

    if (
        Number(onlineWinner) ===
        Number(onlinePlayer)
    ) {

        result.textContent = onlineAbandonment
            ? "🏆 OU GENYEN — adversaire a kite match la."
            : "🏆 OU GENYEN";

        return;
    }

    result.textContent = onlineAbandonment
        ? "❌ OU PÈDI — ou kite match la."
        : "❌ OU PÈDI";
}

/* ==================================================
   NOUVELLE PARTIE
================================================== */

function updateOnlineNewGameButton() {
    const button = document.getElementById("onlineNewGame");
    if (button) {
        button.style.display = "none";
    }
}

/* ==================================================
   RENDER ONLINE
================================================== */

function renderOnlineState() {

    const container =
        document.getElementById(
            "onlineBoard"
        );

    if (!container) {
        return;
    }

    let boardElement =
        container.querySelector(
            ".board"
        );

    if (!boardElement) {

        createBoard(
            container,
            onlineClick
        );

        boardElement =
            container.querySelector(
                ".board"
            );
    }

    if (!boardElement) {
        return;
    }

    for (
        let row = 0;
        row < BOARD_SIZE;
        row++
    ) {

        for (
            let col = 0;
            col < BOARD_SIZE;
            col++
        ) {

            const index =
                row * BOARD_SIZE + col;

            const cell =
                boardElement.querySelector(`.cell[data-row="${row}"][data-col="${col}"]`);

            if (!cell) {
                continue;
            }

            const key =
                row + "," + col;

            cell.innerHTML = "";

            if (onlineBoardState[key]) {
                drawStone(cell, onlineBoardState[key]);
                if (onlineLastMove && Number(onlineLastMove.row) === row && Number(onlineLastMove.col) === col) {
                    cell.classList.add("last-move-cell");
                    const lastStone = cell.querySelector(".stone");
                    if (lastStone) lastStone.classList.add("last-move-stone");
                } else {
                    cell.classList.remove("last-move-cell");
                }
            } else {
                cell.classList.remove("last-move-cell");
            }
        }
    }

    clearWinningLine(
        "onlineBoard"
    );

    if (
        onlineGameOver &&
        Array.isArray(
            onlineWinningLine
        ) &&
        onlineWinningLine.length === 5
    ) {

        drawWinningLine(
            "onlineBoard",
            onlineWinningLine
        );
    }
}

/* ==================================================
   REJWE CORRIGÉ
================================================== */

function updateRematchUI() {

    const box = document.getElementById("rematchBox");
    const message = document.getElementById("rematchMessage");
    const actions = document.getElementById("rematchActions");

    if (!box || !message || !actions) return;

    box.style.visibility = "hidden";
    message.textContent = "";
    actions.innerHTML = "";

    if (onlineConnectionMode === "spectator" || !onlineGameOver) {
        return;
    }

    if (onlineRematchRequest !== null) {
        box.style.visibility = "visible";
        const requester = Number(onlineRematchRequest);

        if (requester === Number(onlinePlayer)) {
            message.textContent = "⏳ Demande de revanche envoyée. En attente de l'adversaire.";
            return;
        }

        message.textContent = "🔄 Votre adversaire demande une revanche.";

        const accept = document.createElement("button");
        accept.type = "button";
        accept.className = "rematch-button rematch-accept";
        accept.textContent = "✅ Accepter";
        accept.addEventListener("click", function() { sendRematchResponse(true); });

        const refuse = document.createElement("button");
        refuse.type = "button";
        refuse.className = "rematch-button rematch-refuse";
        refuse.textContent = "❌ Refuser";
        refuse.addEventListener("click", function() { sendRematchResponse(false); });

        actions.appendChild(accept);
        actions.appendChild(refuse);
        return;
    }

    if (Number(onlinePlayer) === 1 || Number(onlinePlayer) === 2) {
        box.style.visibility = "visible";
        message.textContent = "Demandez une revanche à votre adversaire.";

        const request = document.createElement("button");
        request.type = "button";
        request.className = "rematch-button rematch-request";
        request.textContent = "🔄 Demander une revanche";
        request.addEventListener("click", requestRematch);
        actions.appendChild(request);
    }
}

function requestRematch() {
    if (!socket || socket.readyState !== WebSocket.OPEN || !onlineRoom) return;
    if (!onlineGameOver) return;

    socket.send(JSON.stringify({
        type: "rematch_request",
        room: onlineRoom
    }));
}

function sendRematchResponse(
    accepted
) {

    if (
        !socket ||
        socket.readyState !==
        WebSocket.OPEN
    ) {
        return;
    }

    if (!onlineRoom) {
        return;
    }

    socket.send(
        JSON.stringify({
            type:
                "rematch_response",
            room:
                onlineRoom,
            accepted:
                Boolean(accepted)
        })
    );
}

/* ==================================================
   DEMANDE REJWE PANDAN MATCH LA
================================================== */

function updateUndoUI() {

    const box = document.getElementById("undoBox");
    const message = document.getElementById("undoMessage");
    const actions = document.getElementById("undoActions");

    if (!box || !message || !actions) return;

    box.style.visibility = "hidden";
    message.textContent = "";
    actions.innerHTML = "";

    if (onlineConnectionMode === "spectator" || onlineGameOver) {
        return;
    }

    if (onlineUndoRequest !== null) {
        box.style.visibility = "visible";

        if (Number(onlineUndoRequest) === Number(onlinePlayer)) {
            message.textContent = "⏳ Demande de rejwe envoyée. En attente de l'adversaire.";
            return;
        }

        message.textContent = "🔄 Votre adversaire demande d'annuler son dernier pion.";

        const accept = document.createElement("button");
        accept.type = "button";
        accept.className = "undo-button undo-accept";
        accept.textContent = "✅ Accepter";
        accept.addEventListener("click", function() { sendUndoResponse(true); });

        const refuse = document.createElement("button");
        refuse.type = "button";
        refuse.className = "undo-button undo-refuse";
        refuse.textContent = "❌ Refuser";
        refuse.addEventListener("click", function() { sendUndoResponse(false); });

        actions.appendChild(accept);
        actions.appendChild(refuse);
        return;
    }

    if (!onlineLastMove || Number(onlineLastMove.player) !== Number(onlinePlayer)) {
        return;
    }

    box.style.display = "flex";
    box.style.visibility = "visible";
    message.textContent = "Vous pouvez demander l'annulation de votre dernier pion.";

    const request = document.createElement("button");
    request.type = "button";
    request.className = "undo-button undo-request";
    request.textContent = "🔄 Demande rejwe";
    request.addEventListener("click", requestUndo);
    actions.appendChild(request);
}

function requestUndo() {
    if (!socket || socket.readyState !== WebSocket.OPEN || !onlineRoom) return;
    if (onlineConnectionMode === "spectator" || onlineGameOver) return;
    if (!onlineLastMove || Number(onlineLastMove.player) !== Number(onlinePlayer)) return;
    if (onlineUndoRequest !== null) return;

    socket.send(JSON.stringify({
        type: "undo_request",
        room: onlineRoom
    }));
}

function sendUndoResponse(accepted) {
    if (!socket || socket.readyState !== WebSocket.OPEN || !onlineRoom) return;
    if (onlineUndoRequest === null || Number(onlineUndoRequest) === Number(onlinePlayer)) return;

    socket.send(JSON.stringify({
        type: "undo_response",
        room: onlineRoom,
        accepted: Boolean(accepted)
    }));
}

/* ==================================================
   CLICK ONLINE
================================================== */

function onlineClick(
    row,
    col,
    cell
) {

    if (onlineConnectionMode === "spectator" || Number(onlinePlayer) === 0) {
        document.getElementById("gameOnlineError").textContent =
            "👁️ Mode spectateur : vous ne pouvez pas jouer.";
        return;
    }

    if (onlineGameOver) {
        return;
    }

    if (
        onlineRematchRequest !== null
    ) {

        document
            .getElementById(
                "gameOnlineError"
            )
            .textContent =
            "⏳ Attendez la réponse au rejwe.";

        return;
    }

    if (
        !socket ||
        socket.readyState !==
        WebSocket.OPEN
    ) {

        document
            .getElementById(
                "gameOnlineError"
            )
            .textContent =
            "Connexion en cours...";

        return;
    }

    if (!onlineRoom) {
        return;
    }

    if (
        Number(onlineTurn) !==
        Number(onlinePlayer)
    ) {

        document
            .getElementById(
                "gameOnlineError"
            )
            .textContent =
            "Ce n'est pas ton tour.";

        return;
    }

    const key =
        row + "," + col;

    if (
        onlineBoardState[key]
    ) {
        return;
    }

    document
        .getElementById(
            "gameOnlineError"
        )
        .textContent = "";

    socket.send(
        JSON.stringify({
            type:
                "move",
            room:
                onlineRoom,
            row:
                row,
            col:
                col
        })
    );
}

/* ==================================================
   CRÉER AVEC UN AMI
================================================== */

document
    .getElementById("createBtn")
    .addEventListener(
        "click",
        function() {

            document
                .getElementById(
                    "onlineError"
                )
                .textContent = "";

            onlinePlayer = null;
            onlineRoom = null;

            onlineBoardState = {};
            onlinePlayersState = {};

            onlineSessionToken = null;
            onlineConnectionMode =
                "create";

            onlineBlackScore = 0;
            onlineRedScore = 0;

            onlineGameNumber = 1;

            onlineTurn = 1;
            onlineStarter = 1;

            onlineWinner = null;
            onlineGameOver = false;
            onlineDraw = false;

            onlineBlackTime =
                START_TIME;

            onlineRedTime =
                START_TIME;

            onlineLastMove = null;
            onlineRematchRequest =
                null;
            onlineUndoRequest = null;

            onlineWinningLine =
                null;

            connectServer(
                function() {

                    socket.send(
                        JSON.stringify({
                            type:
                                "create"
                        })
                    );
                }
            );
        }
    );

/* ==================================================
   REJOINDRE AVEC CODE
================================================== */

document
    .getElementById("joinBtn")
    .addEventListener(
        "click",
        function() {

            const code =
                document
                    .getElementById(
                        "roomInput"
                    )
                    .value
                    .trim()
                    .toUpperCase();

            if (
                code.length !== 6
            ) {

                document
                    .getElementById(
                        "onlineError"
                    )
                    .textContent =
                    "Le code doit contenir 6 caractères.";

                return;
            }

            document
                .getElementById(
                    "onlineError"
                )
                .textContent = "";

            onlinePlayer = null;
            onlineRoom = code;

            onlineBoardState = {};
            onlinePlayersState = {};

            onlineSessionToken = null;
            onlineConnectionMode =
                "join";

            onlineBlackScore = 0;
            onlineRedScore = 0;

            onlineGameNumber = 1;

            onlineTurn = 1;
            onlineStarter = 1;

            onlineWinner = null;
            onlineGameOver = false;
            onlineDraw = false;

            onlineBlackTime =
                START_TIME;

            onlineRedTime =
                START_TIME;

            onlineLastMove = null;
            onlineRematchRequest =
                null;
            onlineUndoRequest = null;

            onlineWinningLine =
                null;

            connectServer(
                function() {

                    socket.send(
                        JSON.stringify({
                            type:
                                "join",
                            room:
                                code
                        })
                    );
                }
            );
        }
    );

/* ==================================================
   NOUVELLE PARTIE ONLINE
================================================== */

document
    .getElementById("onlineNewGame")
    .addEventListener(
        "click",
        function() {

            if (!onlineGameOver) {
                return;
            }

            if (
                onlineRematchRequest !== null
            ) {
                return;
            }

            if (
                !socket ||
                socket.readyState !==
                WebSocket.OPEN
            ) {

                document
                    .getElementById(
                        "gameOnlineError"
                    )
                    .textContent =
                    "Connexion en cours...";

                return;
            }

            if (!onlineRoom) {
                return;
            }

            socket.send(
                JSON.stringify({
                    type:
                        "reset",
                    room:
                        onlineRoom
                })
            );
        }
    );

/* ==================================================
   RECONNECT
================================================== */

function scheduleReconnect() {

    if (
        !onlineRoom ||
        !onlineSessionToken ||
        !onlinePlayer
    ) {
        return;
    }

    if (reconnecting) {
        return;
    }

    reconnecting = true;

    reconnectAttempts++;

    const delay =
        Math.min(
            1000 *
            Math.pow(
                2,
                reconnectAttempts - 1
            ),
            10000
        );

    const status =
        document.getElementById(
            "onlineStatus"
        );

    if (status) {

        status.textContent =
            "Connexion perdue... reconnexion...";
    }

    reconnectTimer =
        setTimeout(
            function() {

                reconnecting = false;

                reconnectToRoom();

            },
            delay
        );
}

function reconnectToRoom() {

    if (
        !onlineRoom ||
        !onlineSessionToken ||
        !onlinePlayer
    ) {
        return;
    }

    if (
        socket &&
        (
            socket.readyState ===
            WebSocket.OPEN ||
            socket.readyState ===
            WebSocket.CONNECTING
        )
    ) {
        return;
    }

    const room =
        onlineRoom;

    const player =
        onlinePlayer;

    const token =
        onlineSessionToken;

    connectServer(
        function() {

            socket.send(
                JSON.stringify({
                    type:
                        "reconnect",
                    room:
                        room,
                    player:
                        player,
                    session_token:
                        token
                })
            );
        }
    );
}

/* ==================================================
   RETOUR ONLINE
================================================== */

document
    .getElementById("onlineBack")
    .addEventListener(
        "click",
        function() {

            closeOnlineConnection();

            // Quand le joueur est connecté, Retour ramène au vrai accueil du compte.
            showScreen(accountConnected ? "accountMenuScreen" : "localScreen");
        }
    );

document.getElementById("leaveOnlineMatchBtn")?.addEventListener("click", function() {
    if (!onlineRoom || onlineConnectionMode === "spectator") {
        // Spectatè a kite sèlman match la; li rete konekte pou l ka resevwa envitasyon.
        if (socket && socket.readyState === WebSocket.OPEN && onlineRoom) {
            socket.send(JSON.stringify({type:"stop_watching", room:onlineRoom}));
        }
    } else if (socket && socket.readyState === WebSocket.OPEN) {
        socket.send(JSON.stringify({type:"leave_match", room:onlineRoom}));
    }
    stopOnlineDisplayTimer();
    if (reconnectTimer) { clearTimeout(reconnectTimer); reconnectTimer = null; }
    reconnecting = false; reconnectAttempts = 0;
    onlinePlayer = null; onlineRoom = null; onlineSessionToken = null;
    onlineConnectionMode = null; onlineLastMove = null; onlineRematchRequest = null; onlineUndoRequest = null;
    onlineBoardState = {}; onlinePlayersState = {}; onlineWinner = null; onlineGameOver = false; onlineDraw = false;
    showScreen(accountConnected ? "accountMenuScreen" : "localScreen");
    if (accountConnected) {
        connectServer(function(){
            if (socket && socket.readyState === WebSocket.OPEN) socket.send(JSON.stringify({type:"online_players"}));
        });
    }
});

document
    .getElementById("onlineGameBack")
    .addEventListener(
        "click",
        function() {

            closeOnlineConnection();

            // Quand le joueur est connecté, Retour ramène au vrai accueil du compte.
            showScreen(accountConnected ? "accountMenuScreen" : "localScreen");
        }
    );

/* ==================================================
   FERMER ONLINE
================================================== */

function closeOnlineConnection() {

    hideGameInvite();
    onlinePlayersList = [];

    searchingForOpponent =
        false;

    stopOnlineDisplayTimer();

    if (reconnectTimer) {

        clearTimeout(
            reconnectTimer
        );

        reconnectTimer = null;
    }

    reconnecting = false;
    reconnectAttempts = 0;

    if (
        socket &&
        socket.readyState !==
        WebSocket.CLOSED
    ) {

        try {
            socket.close();
        } catch(error) {
        }
    }

    socket = null;

    onlinePlayer = null;
    onlineRoom = null;

    onlineBoardState = {};
    onlinePlayersState = {};

    onlineTurn = 1;
    onlineStarter = 1;

    onlineWinner = null;
    onlineGameOver = false;
    onlineDraw = false;
    onlineAbandonment = false;

    onlineBlackTime =
        START_TIME;

    onlineRedTime =
        START_TIME;

    onlineBlackScore = 0;
    onlineRedScore = 0;

    onlineGameNumber = 1;

    onlineWinningLine =
        null;

    onlineLastMove = null;
    onlineRematchRequest =
        null;

    onlineSessionToken = null;
    onlineConnectionMode = null;

    document
        .getElementById(
            "searchingBox"
        )
        .classList.remove(
            "show"
        );

    document
        .getElementById(
            "friendBox"
        )
        .classList.remove(
            "show"
        );

    document
        .getElementById(
            "roomCode"
        )
        .textContent =
        "---";

    document
        .getElementById(
            "playerNumber"
        )
        .textContent =
        "---";

    document
        .getElementById(
            "gameRoomCode"
        )
        .textContent =
        "---";

    document
        .getElementById(
            "onlineBlackScore"
        )
        .textContent =
        "0";

    document
        .getElementById(
            "onlineRedScore"
        )
        .textContent =
        "0";

    document
        .getElementById(
            "onlineBlackTime"
        )
        .textContent =
        "10:00";

    document
        .getElementById(
            "onlineRedTime"
        )
        .textContent =
        "10:00";

    document
        .getElementById(
            "onlineError"
        )
        .textContent = "";

    document
        .getElementById(
            "gameOnlineError"
        )
        .textContent = "";

    document
        .getElementById(
            "onlineResult"
        )
        .textContent = "";

    document
        .getElementById(
            "onlineResult"
        )
        .classList.remove(
            "show"
        );

    const blackName = document.getElementById("onlineBlackName");
    const redName = document.getElementById("onlineRedName");
    const spectatorCount = document.getElementById("onlineSpectatorCount");
    const notice = document.getElementById("onlineMatchNotice");

    if (blackName) blackName.textContent = "Joueur 1";
    if (redName) redName.textContent = "Joueur 2";
    if (spectatorCount) spectatorCount.textContent = "👁️ Spectateurs : 0";
    if (notice) notice.textContent = "";

    document
        .getElementById(
            "onlineNewGame"
        )
        .style.display =
        "none";

    clearWinningLine(
        "onlineBoard"
    );

    updateRematchUI();
}

/* ==================================================
   TIMERS GLOBAL
================================================== */

function stopAllTimers() {

    stopLocalTimer();
    stopRobotTimer();
    stopOnlineDisplayTimer();
}



/* ==================================================
   PORTEFEUILLE / DEFIS — MODE TEST
================================================== */
const DEMO_KEY = "mrjery_wallet_demo_v1";
const defaultDemo = {usd:0,htg:0,fees:0,matches:0,commission:10,history:[]};
function demoState(){try{return Object.assign({},defaultDemo,JSON.parse(localStorage.getItem(DEMO_KEY)||"{}"));}catch(e){return {...defaultDemo};}}
function saveDemoState(s){localStorage.setItem(DEMO_KEY,JSON.stringify(s));}
function money(v,c){return c === "HTG" ? Number(v).toFixed(2)+" HTG" : "$"+Number(v).toFixed(2)+" USD";}
function renderWallet(){const s=demoState(); document.getElementById("demoUsd").textContent=money(s.usd,"USD"); document.getElementById("demoHtg").textContent=money(s.htg,"HTG"); document.getElementById("demoFees").textContent=money(s.fees,"USD"); document.getElementById("adminFee").textContent=Number(s.commission).toFixed(1)+"%"; document.getElementById("adminMatches").textContent=s.matches; document.getElementById("adminRevenue").textContent=money(s.fees,"USD"); const h=document.getElementById("walletHistory"); h.innerHTML=s.history.length?s.history.slice().reverse().map(x=>`<div class="history-item">${x}</div>`).join(""): '<div class="history-item">Aucune transaction en mode test.</div>';}
function calcBet(){const amount=Math.max(0,Number(document.getElementById("betAmount").value)||0), c=document.getElementById("betCurrency").value, feePct=demoState().commission, total=amount*2, fee=total*feePct/100, winner=total-fee; document.getElementById("calcA").textContent=money(amount,c);document.getElementById("calcB").textContent=money(amount,c);document.getElementById("calcTotal").textContent=money(total,c);document.getElementById("calcFee").textContent=money(fee,c);document.getElementById("calcWinner").textContent=money(winner,c);}
document.getElementById("walletBtn")?.addEventListener("click",()=>{if(!accountConnected){showScreen("accountScreen");showAccountMessage("Connectez-vous pour accéder au portefeuille.",false);return;}renderWallet();showScreen("walletScreen");});
document.getElementById("walletBack")?.addEventListener("click",()=>showAccountMenu());
document.getElementById("createBetBtn")?.addEventListener("click",()=>{document.getElementById("betCreatorBox").style.display="block";calcBet();});
document.getElementById("cancelBetBtn")?.addEventListener("click",()=>document.getElementById("betCreatorBox").style.display="none");
document.getElementById("betAmount")?.addEventListener("input",calcBet);
document.getElementById("betCurrency")?.addEventListener("change",calcBet);
document.getElementById("confirmBetBtn")?.addEventListener("click",()=>{const s=demoState(), opp=document.getElementById("betOpponent").value.trim(), amount=Number(document.getElementById("betAmount").value)||0, c=document.getElementById("betCurrency").value;if(!opp||amount<=0){document.getElementById("walletMessage").textContent="Indiquez un adversaire et un montant valide.";return;}const total=amount*2,fee=total*s.commission/100;s.matches++;s.fees += c==="USD"?fee:0;s.history.push(`Défi TEST créé contre ${opp} — ${money(amount,c)} chacun — commission prévue ${money(fee,c)}`);saveDemoState(s);renderWallet();document.getElementById("betCreatorBox").style.display="none";document.getElementById("walletMessage").textContent="Défi enregistré en mode test. Aucun paiement réel n'a été effectué.";});
document.getElementById("refreshWalletBtn")?.addEventListener("click",renderWallet);
document.getElementById("withdrawBtn")?.addEventListener("click",()=>{document.getElementById("walletMessage").textContent="Le retrait réel sera activé uniquement après connexion à un prestataire de paiement autorisé et au backend sécurisé.";});
document.getElementById("saveAdminBtn")?.addEventListener("click",()=>{const s=demoState();s.commission=Math.min(100,Math.max(0,Number(document.getElementById("adminCommission").value)||0));saveDemoState(s);renderWallet();});


/* ==================================================
   LANDING / LANGUAGE / AUTH NAVIGATION
================================================== */
const landingTranslations={
 fr:{navHome:'Accueil',navGame:'Jeu',navAbout:'À propos',heroTitle:'Plus qu’un jeu... une communauté !',heroText:'Affronte des joueurs du monde entier, relève des défis, progresse et deviens le meilleur sur MR_Jery Morpion.',fGlobal:'Joueurs du monde entier',fSecure:'Sécurisé & fiable',fFast:'Rapide & fluide',fRewards:'Défis & récompenses',login:'Connexion',register:'Créer un compte',about:'À propos',cardOnline:'Jouer en ligne',cardOnlineText:'Défie des joueurs de tous les pays.',cardSecurity:'Sécurité',cardSecurityText:'Protection pour ton compte et tes parties.',cardCommunity:'Communauté',cardCommunityText:'Rencontre de nouveaux joueurs.',cardFast:'Rapide',cardFastText:'Des matchs fluides, sans complication.',cardChallenge:'Défis',cardChallengeText:'Montre ta valeur sur le plateau.',footer:'Joue • Défie • Gagne',aboutTitle:'Plus qu’un jeu... une communauté !',aboutText:'MR_Jery Morpion est une plateforme pour jouer, rencontrer des joueurs, relever des défis et suivre ta progression.',vision:'Vision',visionText:'Rassembler les joueurs de morpion du monde entier.',mission:'Mission',missionText:'Offrir une expérience rapide, simple et agréable.',values:'Valeurs',valuesText:'Respect, fair-play, communauté et évolution.'},
 en:{navHome:'Home',navGame:'Game',navAbout:'About',heroTitle:'More than a game... a community!',heroText:'Face players from around the world, take on challenges, compete and climb MR_Jery Morpion.',fGlobal:'Players worldwide',fSecure:'Secure & reliable',fFast:'Fast & fluid',fRewards:'Challenges & rewards',login:'Login',register:'Create an account',about:'About',cardOnline:'Play Online',cardOnlineText:'Challenge players worldwide.',cardSecurity:'Security',cardSecurityText:'Protection for your account and games.',cardCommunity:'Community',cardCommunityText:'Meet new players and opponents.',cardFast:'Fast',cardFastText:'Smooth matches, no hassle.',cardChallenge:'Challenges',cardChallengeText:'Show your skills on the board.',footer:'Play • Challenge • Win',aboutTitle:'More than a game... a community!',aboutText:'MR_Jery Morpion is a platform to play, meet players, take on challenges and track your progress.',vision:'Vision',visionText:'Bring morpion players together worldwide.',mission:'Mission',missionText:'Offer a fast, simple and enjoyable experience.',values:'Values',valuesText:'Respect, fair play, community and growth.'},
 es:{navHome:'Inicio',navGame:'Juego',navAbout:'Acerca de',heroTitle:'Más que un juego... ¡una comunidad!',heroText:'Enfréntate a jugadores de todo el mundo, acepta desafíos y progresa en MR_Jery Morpion.',fGlobal:'Jugadores de todo el mundo',fSecure:'Seguro y fiable',fFast:'Rápido y fluido',fRewards:'Desafíos y recompensas',login:'Iniciar sesión',register:'Crear una cuenta',about:'Acerca de',cardOnline:'Jugar en línea',cardOnlineText:'Desafía a jugadores de todo el mundo.',cardSecurity:'Seguridad',cardSecurityText:'Protección para tu cuenta y partidas.',cardCommunity:'Comunidad',cardCommunityText:'Conoce nuevos jugadores.',cardFast:'Rápido',cardFastText:'Partidas fluidas y sencillas.',cardChallenge:'Desafíos',cardChallengeText:'Demuestra tus habilidades.',footer:'Juega • Desafía • Gana',aboutTitle:'Más que un juego... ¡una comunidad!',aboutText:'MR_Jery Morpion es una plataforma para jugar, conocer jugadores, aceptar desafíos y seguir tu progreso.',vision:'Visión',visionText:'Reunir a jugadores de todo el mundo.',mission:'Misión',missionText:'Ofrecer una experiencia rápida, sencilla y divertida.',values:'Valores',valuesText:'Respeto, juego limpio, comunidad y evolución.'},
 ht:{navHome:'Akèy',navGame:'Jwèt',navAbout:'A Pwopo',heroTitle:'Plis pase yon jwèt... yon kominote!',heroText:'Jwe ak moun ki soti nan tout mond lan, leve defi, fè konpetisyon epi monte nan MR_Jery Morpion.',fGlobal:'Jwè nan tout mond lan',fSecure:'Sekirize & serye',fFast:'Rapid & fluid',fRewards:'Defi & rekonpans',login:'Konekte',register:'Kreye yon kont',about:'A pwopo',cardOnline:'Jouer en ligne',cardOnlineText:'Défie des joueurs de tous les pays.',cardSecurity:'Sekirite',cardSecurityText:'Pwoteksyon pou kont ou ak jwèt yo.',cardCommunity:'Kominote',cardCommunityText:'Rankontre nouvo jwè ak advèsè.',cardFast:'Rapid',cardFastText:'Match fluid, san konplikasyon.',cardChallenge:'Defi',cardChallengeText:'Montre kapasite w sou tablo a.',footer:'Jwe • Defi • Gagne',aboutTitle:'Plis pase yon jwèt... yon kominote!',aboutText:'MR_Jery Morpion se yon platfòm pou jwe, rankontre jwè, leve defi epi suiv pwogrè ou.',vision:'Vizyon',visionText:'Rasanble jwè morpion atravè mond lan.',mission:'Misyon',missionText:'Bay yon eksperyans rapid, senp ak agreyab.',values:'Valè',valuesText:'Respè, fair-play, kominote ak evolisyon.'},
 pt:{navHome:'Início',navGame:'Jogo',navAbout:'Sobre',heroTitle:'Mais que um jogo... uma comunidade!',heroText:'Enfrente jogadores do mundo inteiro, aceite desafios e avance no MR_Jery Morpion.',fGlobal:'Jogadores do mundo inteiro',fSecure:'Seguro e confiável',fFast:'Rápido e fluido',fRewards:'Desafios e recompensas',login:'Entrar',register:'Criar uma conta',about:'Sobre',cardOnline:'Jogar online',cardOnlineText:'Desafie jogadores do mundo inteiro.',cardSecurity:'Segurança',cardSecurityText:'Proteção para sua conta e partidas.',cardCommunity:'Comunidade',cardCommunityText:'Conheça novos jogadores.',cardFast:'Rápido',cardFastText:'Partidas fluidas e simples.',cardChallenge:'Desafios',cardChallengeText:'Mostre suas habilidades.',footer:'Jogue • Desafie • Vença',aboutTitle:'Mais que um jogo... uma comunidade!',aboutText:'MR_Jery Morpion é uma plataforma para jogar, conhecer jogadores, aceitar desafios e acompanhar seu progresso.',vision:'Visão',visionText:'Reunir jogadores de morpion do mundo inteiro.',mission:'Missão',missionText:'Oferecer uma experiência rápida, simples e agradável.',values:'Valores',valuesText:'Respeito, fair play, comunidade e evolução.'}
};
const fullSiteTextTranslations={
  'Jwe Anliy':{fr:'Jouer en ligne',en:'Play Online',ht:'Jwe Anliy'},
  'Jwe ak yon zanmi':{fr:'Jouer avec un ami',en:'Play with a Friend',ht:'Jwe ak yon zanmi'},
  'Defi':{fr:'Défis',en:'Challenges',ht:'Defi'},
  'Paryaj':{fr:'Paris',en:'Bets',ht:'Paryaj'},
  'Spectateur':{fr:'Spectateurs',en:'Spectators',ht:'Espektatè'},
  'Robot':{fr:'Robot',en:'Robot',ht:'Robo'},
  'Classement':{fr:'Classement',en:'Leaderboard',ht:'Klasman'},
  'Affronte des joueurs du monde entier.':{fr:'Affronte des joueurs du monde entier.',en:'Challenge players from around the world.',ht:'Defi jwè ki soti toupatou nan mond lan.'},
  'Envite yon zanmi epi jwe ansanm.':{fr:'Invite un ami et jouez ensemble.',en:'Invite a friend and play together.',ht:'Envite yon zanmi epi jwe ansanm.'},
  'Kreye oswa aksepte defi.':{fr:'Crée ou accepte des défis.',en:'Create or accept challenges.',ht:'Kreye oswa aksepte defi.'},
  'Mise, jwe epi suiv rekonpans yo.':{fr:'Mise, joue et suis tes récompenses.',en:'Place bets, play, and track rewards.',ht:'Mize, jwe epi suiv rekonpans yo.'},
  'Gade match yo an dirèk.':{fr:'Regarde les matchs en direct.',en:'Watch matches live.',ht:'Gade match yo an dirèk.'},
  'Jwe kont IA a pou antrene.':{fr:'Joue contre l’IA pour t’entraîner.',en:'Play against the AI to practice.',ht:'Jwe kont IA a pou antrene.'},
  'Gade pi bon jwè yo.':{fr:'Découvre les meilleurs joueurs.',en:'See the top players.',ht:'Gade pi bon jwè yo.'},
  'Tout jwèt platfòm nan nan yon sèl meni.':{fr:'Tous les jeux de la plateforme dans un seul menu.',en:'All platform games in one menu.',ht:'Tout jwèt platfòm nan nan yon sèl meni.'},
  'Solde USD':{fr:'Solde USD',en:'USD Balance',ht:'Balans USD'},
  'Solde HTG':{fr:'Solde HTG',en:'HTG Balance',ht:'Balans HTG'},
  'Joueur MR_Jery':{fr:'Joueur MR_Jery',en:'MR_Jery Player',ht:'Jwè MR_Jery'},
  'Connecté':{fr:'Connecté',en:'Signed in',ht:'Konekte'},
  'Jwe • Defi • Gagne':{fr:'Joue • Défie • Gagne',en:'Play • Challenge • Win',ht:'Jwe • Defi • Genyen'},
  'Defi e jwè nan tout peyi.':{fr:'Défie des joueurs de tous les pays.',en:'Challenge players worldwide.',ht:'Defi jwè nan tout peyi.'},
  'Sekirite':{fr:'Sécurité',en:'Security',ht:'Sekirite'},
  'Pwoteksyon pou kont ou ak jwèt yo.':{fr:'Protection de ton compte et de tes parties.',en:'Protection for your account and games.',ht:'Pwoteksyon pou kont ou ak jwèt yo.'},
  'Kominote':{fr:'Communauté',en:'Community',ht:'Kominote'},
  'Rankontre jwè ak nouvo advèsè.':{fr:'Rencontre de nouveaux joueurs et adversaires.',en:'Meet new players and opponents.',ht:'Rankontre nouvo jwè ak advèsè.'},
  'Rapid':{fr:'Rapide',en:'Fast',ht:'Rapid'},
  'Match vit, san konplikasyon.':{fr:'Des matchs rapides et simples.',en:'Fast, hassle-free matches.',ht:'Match rapid, san konplikasyon.'},
  'Montre kapasite w sou tablo a.':{fr:'Montre tes compétences sur le plateau.',en:'Show your skills on the board.',ht:'Montre kapasite w sou tablo a.'}
};
Object.assign(fullSiteTextTranslations, {
 'Connexion':{fr:'Connexion',en:'Login',ht:'Konekte'}, 'Créer un compte':{fr:'Créer un compte',en:'Create an account',ht:'Kreye yon kont'},
 'Accueil':{fr:'Accueil',en:'Home',ht:'Akèy'}, 'Jeu':{fr:'Jeu',en:'Game',ht:'Jwèt'}, 'À propos':{fr:'À propos',en:'About',ht:'A pwopo'},
 'Jouer avec un ami':{fr:'Jouer avec un ami',en:'Play with a Friend',ht:'Jwe ak yon zanmi'}, 'Spectateur':{fr:'Spectateurs',en:'Spectators',ht:'Espektatè'},
 'Mon profil':{fr:'Mon profil',en:'My Profile',ht:'Pwofil mwen'}, 'Profil':{fr:'Profil',en:'Profile',ht:'Pwofil'}, 'Wallet':{fr:'Portefeuille',en:'Wallet',ht:'Bous'},
 'Déconnexion':{fr:'Déconnexion',en:'Log out',ht:'Dekonekte'}, 'Classement':{fr:'Classement',en:'Leaderboard',ht:'Klasman'},
 'Affronte des joueurs du monde entier.':{fr:'Affronte des joueurs du monde entier.',en:'Challenge players around the world.',ht:'Defi jwè toupatou nan mond lan.'},
 'Jwe ak yon zanmi':{fr:'Jouer avec un ami',en:'Play with a Friend',ht:'Jwe ak yon zanmi'}, 'Defi':{fr:'Défis',en:'Challenges',ht:'Defi'}, 'Paryaj':{fr:'Paris',en:'Bets',ht:'Paryaj'},
 'Créer un compte':{fr:'Créer un compte',en:'Create an account',ht:'Kreye yon kont'}, 'Connexion':{fr:'Connexion',en:'Login',ht:'Konekte'},
 "Connecte-toi à ton compte":{fr:'Connecte-toi à ton compte',en:'Sign in to your account',ht:'Konekte sou kont ou'},
 "Nom d'utilisateur ou e-mail":{fr:"Nom d'utilisateur ou e-mail",en:'Username or email',ht:'Non itilizatè oswa imèl'},
 "Nom d'utilisateur":{fr:"Nom d'utilisateur",en:'Username',ht:'Non itilizatè'}, 'Mot de passe':{fr:'Mot de passe',en:'Password',ht:'Modpas'},
 'Confirmer le mot de passe':{fr:'Confirmer le mot de passe',en:'Confirm password',ht:'Konfime modpas la'}, 'E-mail':{fr:'E-mail',en:'Email',ht:'Imèl'},
 'Pays de résidence':{fr:'Pays de résidence',en:'Country of residence',ht:'Peyi kote w rete'}, 'Langue préférée':{fr:'Langue préférée',en:'Preferred language',ht:'Lang ou prefere'},
 'Se souvenir de moi':{fr:'Se souvenir de moi',en:'Remember me',ht:'Sonje mwen'}, 'Mot de passe oublié ?':{fr:'Mot de passe oublié ?',en:'Forgot password?',ht:'Ou bliye modpas ou?'},
 'Se connecter':{fr:'Se connecter',en:'Sign in',ht:'Konekte'}, 'Se connecter avec Google':{fr:'Se connecter avec Google',en:'Sign in with Google',ht:'Konekte ak Google'},
 'OU':{fr:'OU',en:'OR',ht:'OSWA'}, "Vous n'avez pas de compte ?":{fr:"Vous n'avez pas de compte ?",en:"Don't have an account?",ht:'Ou poko gen kont?'},
 'Vous avez déjà un compte ?':{fr:'Vous avez déjà un compte ?',en:'Already have an account?',ht:'Ou deja gen kont?'},
 "J'accepte les conditions d'utilisation et la politique de confidentialité.":{fr:"J'accepte les conditions d'utilisation et la politique de confidentialité.",en:'I accept the terms of use and privacy policy.',ht:'Mwen aksepte kondisyon itilizasyon yo ak règleman konfidansyalite a.'},
 'Créer mon compte':{fr:'Créer mon compte',en:'Create my account',ht:'Kreye kont mwen'}, 'Retour':{fr:'Retour',en:'Back',ht:'Retounen'},
 'Paramètres':{fr:'Paramètres',en:'Settings',ht:'Paramèt'}, 'Les paramètres du jeu seront ajoutés ici.':{fr:'Les paramètres du jeu seront ajoutés ici.',en:'Game settings will be added here.',ht:'Paramèt jwèt la ap ajoute isit la.'},
 "Pour le moment, aucun réglage supplémentaire n'est nécessaire.":{fr:"Pour le moment, aucun réglage supplémentaire n'est nécessaire.",en:'No additional settings are needed for now.',ht:'Pou kounye a, pa gen lòt paramèt ki nesesè.'},
 'Portefeuille & Défis':{fr:'Portefeuille & Défis',en:'Wallet & Challenges',ht:'Bous ak Defi'}, 'Solde USD':{fr:'Solde USD',en:'USD Balance',ht:'Balans USD'}, 'Solde HTG':{fr:'Solde HTG',en:'HTG Balance',ht:'Balans HTG'},
 'Commissions plateforme':{fr:'Commissions plateforme',en:'Platform fees',ht:'Komisyon platfòm'}, 'Créer un défi':{fr:'Créer un défi',en:'Create a challenge',ht:'Kreye yon defi'},
 'Demander un retrait':{fr:'Demander un retrait',en:'Request a withdrawal',ht:'Mande retrè'}, 'Actualiser':{fr:'Actualiser',en:'Refresh',ht:'Rafrechi'},
 'Nouveau défi':{fr:'Nouveau défi',en:'New challenge',ht:'Nouvo defi'}, 'Mise joueur 1 :':{fr:'Mise joueur 1 :',en:'Player 1 stake:',ht:'Miz jwè 1:'}, 'Mise joueur 2 :':{fr:'Mise joueur 2 :',en:'Player 2 stake:',ht:'Miz jwè 2:'},
 'Total :':{fr:'Total :',en:'Total:',ht:'Total:'}, 'Commission plateforme :':{fr:'Commission plateforme :',en:'Platform fee:',ht:'Komisyon platfòm:'}, 'Montant net du gagnant :':{fr:'Montant net du gagnant :',en:'Winner payout:',ht:'Kob gayan an ap resevwa:'},
 'Annuler':{fr:'Annuler',en:'Cancel',ht:'Anile'}, 'Historique':{fr:'Historique',en:'History',ht:'Istwa'}, 'Aucune transaction en mode test.':{fr:'Aucune transaction en mode test.',en:'No transactions in test mode.',ht:'Pa gen tranzaksyon nan mòd tès la.'},
 'Administration':{fr:'Administration',en:'Administration',ht:'Administrasyon'}, 'Commission':{fr:'Commission',en:'Commission',ht:'Komisyon'}, 'Matchs avec mise':{fr:'Matchs avec mise',en:'Wager matches',ht:'Match ak miz'}, 'Revenus plateforme':{fr:'Revenus plateforme',en:'Platform revenue',ht:'Revni platfòm'}, 'Paramètres de calcul':{fr:'Paramètres de calcul',en:'Calculation settings',ht:'Paramèt kalkil'}, 'Enregistrer':{fr:'Enregistrer',en:'Save',ht:'Anrejistre'},
 'Jouer avec Robot — Niveau MASTER':{fr:'Jouer avec Robot — Niveau MASTER',en:'Play against Robot — MASTER Level',ht:'Jwe kont Robo — Nivo MASTER'}, 'À ton tour — le robot bloque les victoires immédiates et les trois ouverts.':{fr:'À ton tour — le robot bloque les victoires immédiates et les trois ouverts.',en:'Your turn — the robot blocks immediate wins and open threes.',ht:'Se tou pa w — robo a bloke viktwa imedya ak twa ouvè.'},
 '2 Utilisateurs':{fr:'2 joueurs',en:'2 Players',ht:'2 jwè'}, 'Tour du joueur noir':{fr:'Tour du joueur noir',en:'Black player’s turn',ht:'Se tou jwè nwa a'}, 'Jouer en Ligne':{fr:'Jouer en ligne',en:'Play Online',ht:'Jwe Anliy'},
 'Trouver un adversaire':{fr:'Trouver un adversaire',en:'Find an opponent',ht:'Jwenn yon advèsè'}, "Salle d'attente":{fr:"Salle d'attente",en:'Waiting room',ht:'Sal datant'}, 'Regarder un match':{fr:'Regarder un match',en:'Watch a match',ht:'Gade yon match'},
 "Recherche d'un adversaire...":{fr:"Recherche d'un adversaire...",en:'Searching for an opponent...',ht:'N ap chèche yon advèsè...'}, 'Créer une partie':{fr:'Créer une partie',en:'Create a game',ht:'Kreye yon pati'}, 'Rejoindre une partie':{fr:'Rejoindre une partie',en:'Join a game',ht:'Antre nan yon pati'},
 'Paramètres de l’invitation':{fr:'Paramètres de l’invitation',en:'Invitation settings',ht:'Paramèt envitasyon an'}, 'Durée du match':{fr:'Durée du match',en:'Match duration',ht:'Dire match la'}, 'Joueurs en ligne':{fr:'Joueurs en ligne',en:'Players online',ht:'Jwè anliy'}, 'Chargement des joueurs...':{fr:'Chargement des joueurs...',en:'Loading players...',ht:'N ap chaje jwè yo...'},
 'En attente...':{fr:'En attente...',en:'Waiting...',ht:'Ap tann...'}, 'Choisissez un match en direct :':{fr:'Choisissez un match en direct :',en:'Choose a live match:',ht:'Chwazi yon match an dirèk:'}, 'Connexion...':{fr:'Connexion...',en:'Connecting...',ht:'Ap konekte...'},
 'Chat du match':{fr:'Chat du match',en:'Match chat',ht:'Chat match la'}, 'Masquer':{fr:'Masquer',en:'Hide',ht:'Kache'}, 'Voye':{fr:'Envoyer',en:'Send',ht:'Voye'}, 'Mikwo fèmen':{fr:'Micro désactivé',en:'Microphone off',ht:'Mikwo fèmen'},
 'Nouvelle partie':{fr:'Nouvelle partie',en:'New game',ht:'Nouvo pati'}, 'Kite match la':{fr:'Quitter le match',en:'Leave match',ht:'Kite match la'}, 'Retour au menu':{fr:'Retour au menu',en:'Back to menu',ht:'Retounen nan meni an'}, 'Accepter':{fr:'Accepter',en:'Accept',ht:'Aksepte'}, 'Refuser':{fr:'Refuser',en:'Decline',ht:'Refize'}, 'FIN DE PARTIE':{fr:'FIN DE PARTIE',en:'GAME OVER',ht:'MATCH FINI'}, 'Rejouer':{fr:'Rejouer',en:'Play again',ht:'Jwe ankò'},
 'Aucune transaction en mode test.':{fr:'Aucune transaction en mode test.',en:'No transactions in test mode.',ht:'Pa gen tranzaksyon nan mòd tès la.'}
});

Object.assign(fullSiteTextTranslations, {
 '🌐 Jouer en Ligne':{fr:'🌐 Jouer en ligne',en:'🌐 Play Online',ht:'🌐 Jwe Anliy'},
 '🔎 Trouver un adversaire':{fr:'🔎 Trouver un adversaire',en:'🔎 Find an opponent',ht:'🔎 Jwenn yon advèsè'},
 '👥 Jouer avec un ami':{fr:'👥 Jouer avec un ami',en:'👥 Play with a Friend',ht:'👥 Jwe ak yon zanmi'},
 '⏳ Salle d’attente':{fr:'⏳ Salle d’attente',en:'⏳ Waiting Room',ht:'⏳ Sal datant'},
 '👁️ Regarder un match':{fr:'👁️ Regarder un match',en:'👁️ Watch a Match',ht:'👁️ Gade yon match'},
 'Salle d’attente':{fr:'Salle d’attente',en:'Waiting Room',ht:'Sal datant'},
 'Annuler':{fr:'Annuler',en:'Cancel',ht:'Anile'},
 'Créer une partie':{fr:'Créer une partie',en:'Create a Game',ht:'Kreye yon pati'},
 'Rejoindre une partie':{fr:'Rejoindre une partie',en:'Join a Game',ht:'Antre nan yon pati'},
 '⚙️ Paramètres de l’invitation':{fr:'⚙️ Paramètres de l’invitation',en:'⚙️ Invitation Settings',ht:'⚙️ Paramèt envitasyon an'},
 '1 minute':{fr:'1 minute',en:'1 minute',ht:'1 minit'},
 '2 minutes':{fr:'2 minutes',en:'2 minutes',ht:'2 minit'},
 '3 minutes':{fr:'3 minutes',en:'3 minutes',ht:'3 minit'},
 '4 minutes':{fr:'4 minutes',en:'4 minutes',ht:'4 minit'},
 '5 minutes':{fr:'5 minutes',en:'5 minutes',ht:'5 minit'},
 '6 minutes':{fr:'6 minutes',en:'6 minutes',ht:'6 minit'},
 '7 minutes':{fr:'7 minutes',en:'7 minutes',ht:'7 minit'},
 '8 minutes':{fr:'8 minutes',en:'8 minutes',ht:'8 minit'},
 '9 minutes':{fr:'9 minutes',en:'9 minutes',ht:'9 minit'},
 '10 minutes':{fr:'10 minutes',en:'10 minutes',ht:'10 minit'},
 '11 minutes':{fr:'11 minutes',en:'11 minutes',ht:'11 minit'},
 '12 minutes':{fr:'12 minutes',en:'12 minutes',ht:'12 minit'},
 '13 minutes':{fr:'13 minutes',en:'13 minutes',ht:'13 minit'},
 '14 minutes':{fr:'14 minutes',en:'14 minutes',ht:'14 minit'},
 '15 minutes':{fr:'15 minutes',en:'15 minutes',ht:'15 minit'},
 '16 minutes':{fr:'16 minutes',en:'16 minutes',ht:'16 minit'},
 '17 minutes':{fr:'17 minutes',en:'17 minutes',ht:'17 minit'},
 '18 minutes':{fr:'18 minutes',en:'18 minutes',ht:'18 minit'},
 '19 minutes':{fr:'19 minutes',en:'19 minutes',ht:'19 minit'},
 '20 minutes':{fr:'20 minutes',en:'20 minutes',ht:'20 minit'},
 '21 minutes':{fr:'21 minutes',en:'21 minutes',ht:'21 minit'},
 '22 minutes':{fr:'22 minutes',en:'22 minutes',ht:'22 minit'},
 '23 minutes':{fr:'23 minutes',en:'23 minutes',ht:'23 minit'},
 '24 minutes':{fr:'24 minutes',en:'24 minutes',ht:'24 minit'},
 '25 minutes':{fr:'25 minutes',en:'25 minutes',ht:'25 minit'},
 '26 minutes':{fr:'26 minutes',en:'26 minutes',ht:'26 minit'},
 '27 minutes':{fr:'27 minutes',en:'27 minutes',ht:'27 minit'},
 '28 minutes':{fr:'28 minutes',en:'28 minutes',ht:'28 minit'},
 '29 minutes':{fr:'29 minutes',en:'29 minutes',ht:'29 minit'},
 '30 minutes':{fr:'30 minutes',en:'30 minutes',ht:'30 minit'},
 'Gwosè tablo':{fr:'Taille du plateau',en:'Board size',ht:'Gwosè tablo'},
 'Koulè tablo sou telefòn pa w':{fr:'Couleur du plateau sur votre téléphone',en:'Board color on your phone',ht:'Koulè tablo sou telefòn pa w'},
 'Klasik blan':{fr:'Blanc classique',en:'Classic White',ht:'Blan klasik'},
 'Nuit ble':{fr:'Nuit bleue',en:'Blue Night',ht:'Nuit ble'},
 'Vèt mant':{fr:'Vert menthe',en:'Mint Green',ht:'Vèt mant'},
 'Woz dous':{fr:'Rose doux',en:'Soft Pink',ht:'Woz dous'},
 'Sab klè':{fr:'Sable clair',en:'Light Sand',ht:'Sab klè'},
 '👥 Joueurs en ligne':{fr:'👥 Joueurs en ligne',en:'👥 Players Online',ht:'👥 Jwè anliy'},
 'Chargement des joueurs...':{fr:'Chargement des joueurs...',en:'Loading players...',ht:'N ap chaje jwè yo...'},
 '👁️ Regarder un match':{fr:'👁️ Regarder un match',en:'👁️ Watch a Match',ht:'👁️ Gade yon match'},
 'Choisissez un match en direct :':{fr:'Choisissez un match en direct :',en:'Choose a live match:',ht:'Chwazi yon match an dirèk:'},
 '🔄 Actualiser':{fr:'🔄 Actualiser',en:'🔄 Refresh',ht:'🔄 Rafrechi'},
 '🌐 Gomoku en Ligne':{fr:'🌐 Gomoku en ligne',en:'🌐 Online Gomoku',ht:'🌐 Gomoku anliy'},
 '👁️ Spectateurs : 0':{fr:'👁️ Spectateurs : 0',en:'👁️ Spectators: 0',ht:'👁️ Espektatè: 0'},
 'Joueur 1':{fr:'Joueur 1',en:'Player 1',ht:'Jwè 1'}, 'Joueur 2':{fr:'Joueur 2',en:'Player 2',ht:'Jwè 2'},
 '⚫ Noir':{fr:'⚫ Noir',en:'⚫ Black',ht:'⚫ Nwa'}, '🔴 Rouge':{fr:'🔴 Rouge',en:'🔴 Red',ht:'🔴 Wouj'},
 'Chat en direct + communication vocale':{fr:'Chat en direct + communication vocale',en:'Live Chat + Voice Communication',ht:'Chat an dirèk + kominikasyon vokal'},
 '💬 Chat du match':{fr:'💬 Chat du match',en:'💬 Match Chat',ht:'💬 Chat match la'},
 'Masquer':{fr:'Masquer',en:'Hide',ht:'Kache'}, 'Voye':{fr:'Envoyer',en:'Send',ht:'Voye'},
 '🎤 Aktive mikwo':{fr:'🎤 Activer le micro',en:'🎤 Turn on microphone',ht:'🎤 Aktive mikwo'},
 'Mikwo fèmen':{fr:'Micro désactivé',en:'Microphone off',ht:'Mikwo fèmen'},
 'Vwa a disponib ant jwè yo. Spektatè yo ka tande, men yo pa ka pale.':{fr:'La voix est disponible entre les joueurs. Les spectateurs peuvent écouter, mais pas parler.',en:'Voice is available between players. Spectators can listen but cannot speak.',ht:'Vwa a disponib ant jwè yo. Espektatè yo ka tande, men yo pa ka pale.'},
 '🔄 Nouvelle partie':{fr:'🔄 Nouvelle partie',en:'🔄 New Game',ht:'🔄 Nouvo pati'},
 '🚪 Kite match la':{fr:'🚪 Quitter le match',en:'🚪 Leave Match',ht:'🚪 Kite match la'},
 '← Retour au menu':{fr:'← Retour au menu',en:'← Back to Menu',ht:'← Retounen nan meni an'},
 'Code :':{fr:'Code :',en:'Code:',ht:'Kòd:'}, 'Joueur :':{fr:'Joueur :',en:'Player:',ht:'Jwè:'},
 '← Retour':{fr:'← Retour',en:'← Back',ht:'← Retounen'}, 'Retour':{fr:'Retour',en:'Back',ht:'Retounen'},
 'En attente...':{fr:'En attente...',en:'Waiting...',ht:'Ap tann...'}, 'Connecté':{fr:'Connecté',en:'Connected',ht:'Konekte'},
 'Connexion...':{fr:'Connexion...',en:'Connecting...',ht:'Ap konekte...'},
 'Recherche d’un adversaire...':{fr:'Recherche d’un adversaire...',en:'Searching for an opponent...',ht:'N ap chèche yon advèsè...'},
 'Aucun match disponible.':{fr:'Aucun match disponible.',en:'No match available.',ht:'Pa gen match disponib.'},
 'Entrez le code de la partie.':{fr:'Entrez le code de la partie.',en:'Enter the game code.',ht:'Antre kòd pati a.'},
 'Invitation envoyée.':{fr:'Invitation envoyée.',en:'Invitation sent.',ht:'Envitasyon an voye.'},
 'Le joueur a refusé l’invitation.':{fr:'Le joueur a refusé l’invitation.',en:'The player declined the invitation.',ht:'Jwè a refize envitasyon an.'}
});

function translateWholeSiteText(lang){
  const nodes=[];
  const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,{acceptNode(node){
    const parent=node.parentElement;
    if(!parent || parent.closest('script,style,noscript,textarea,option,[contenteditable="true"]')) return NodeFilter.FILTER_REJECT;
    const raw=node.nodeValue, trimmed=raw.trim();
    if(!trimmed) return NodeFilter.FILTER_REJECT;
    return Object.prototype.hasOwnProperty.call(fullSiteTextTranslations,trimmed) || Object.values(fullSiteTextTranslations).some(v=>Object.values(v).includes(trimmed)) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
  }});
  while(walker.nextNode()) nodes.push(walker.currentNode);
  nodes.forEach(node=>{
    const raw=node.nodeValue, trimmed=raw.trim();
    let canonical=trimmed;
    if(!fullSiteTextTranslations[canonical]) canonical=Object.keys(fullSiteTextTranslations).find(k=>Object.values(fullSiteTextTranslations[k]).includes(trimmed))||trimmed;
    const translated=fullSiteTextTranslations[canonical]?.[lang];
    if(translated && translated!==trimmed) node.nodeValue=raw.replace(trimmed,translated);
  });
}
function setLanguage(lang){
  // Se sèlman 3 lang ki disponib pou Morpion: franse (pa defo), anglè, kreyòl.
  if(!['fr','en','ht'].includes(lang)) lang='fr';
  const t=landingTranslations[lang]||landingTranslations.fr;
  document.documentElement.lang=lang;
  translateWholeSiteText(lang);
  try{localStorage.setItem('mrjery_language',lang)}catch(e){}
  document.querySelectorAll('[data-i18n]').forEach(el=>{
    const key=el.dataset.i18n;
    if(!Object.prototype.hasOwnProperty.call(t,key)) return;
    // Kenbe baliz HTML anndan tit yo (pa egzanp <em>) olye efase yo.
    if(key==='heroTitle'||key==='aboutTitle'){
      const title=t[key];
      if(el.querySelector('em')){
        const em=el.querySelector('em');
        const full=el.ownerDocument.createElement('span');
        full.textContent=title;
        el.textContent=''; el.appendChild(full);
      } else el.textContent=title;
    } else el.textContent=t[key];
  });
  const names={fr:'Français',en:'English',ht:'Kreyòl Ayisyen'};
  const n=names[lang];
  ['currentLanguage','aboutCurrentLanguage'].forEach(id=>{const el=document.getElementById(id);if(el)el.textContent=n});
  // Tradui tou tèks ki nan atribi fòm yo (placeholder, title, aria-label)
  // ak opsyon lis yo, san manyen valè itilizatè a deja antre.
  const translateKnown = value => {
    if(!value) return value;
    const trimmed=value.trim();
    let canonical=trimmed;
    if(!fullSiteTextTranslations[canonical]) canonical=Object.keys(fullSiteTextTranslations).find(k=>Object.values(fullSiteTextTranslations[k]).includes(trimmed))||trimmed;
    const result=fullSiteTextTranslations[canonical]?.[lang];
    return result ? value.replace(trimmed,result) : value;
  };
  document.querySelectorAll('input[placeholder],textarea[placeholder], [title], [aria-label]').forEach(el=>{
    for(const attr of ['placeholder','title','aria-label']){
      if(el.hasAttribute(attr)){
        const old=el.getAttribute(attr), next=translateKnown(old);
        if(next!==old) el.setAttribute(attr,next);
      }
    }
  });
  document.querySelectorAll('option').forEach(el=>{
    const old=el.textContent, next=translateKnown(old);
    if(next!==old) el.textContent=next;
  });
  document.getElementById('languageMenu')?.classList.remove('show');
}


function openAuth(mode){showScreen('accountScreen');setAuthMode(mode);}
function setAuthMode(mode){const login=mode==='login';document.getElementById('loginPanel').style.display=login?'block':'none';document.getElementById('registerPanel').style.display=login?'none':'block';document.getElementById('authLoginTab').classList.toggle('active',login);document.getElementById('authRegisterTab').classList.toggle('active',!login);document.getElementById('authTitle').textContent=login?'Connexion':'Créer un compte';document.getElementById('authSubtitle').textContent=login?'Connecte-toi à ton compte':'Rejoins la communauté MR_Jery Morpion';}
let savedLang='fr';try{savedLang=localStorage.getItem('mrjery_language')||'fr'}catch(e){}setLanguage(['fr','en','ht'].includes(savedLang)?savedLang:'fr');
// Re-aplike tradiksyon sou eleman ki parèt pita (meni, mesaj ak ekran dinamik), san modifye lojik jwèt la.
let languageObserverTimer=null;
const languageObserver=new MutationObserver(()=>{if(languageObserverTimer)clearTimeout(languageObserverTimer);languageObserverTimer=setTimeout(()=>{const active=(()=>{try{return localStorage.getItem('mrjery_language')||'fr'}catch(e){return 'fr'}})();const lang=['fr','en','ht'].includes(active)?active:'fr';translateWholeSiteText(lang);translateSiteAttributes(lang);},40);});
languageObserver.observe(document.body,{childList:true,subtree:true,characterData:true,attributes:true,attributeFilter:['placeholder','aria-label','title']});
// Tradui placeholder, titres, aria-label et options de listes san modifye sa itilizatè a ekri.
function translateSiteAttributes(lang){
 const translate=value=>{if(!value)return value;const trimmed=value.trim();const canonical=Object.keys(fullSiteTextTranslations).find(k=>k===trimmed||Object.values(fullSiteTextTranslations[k]).includes(trimmed));const result=canonical&&fullSiteTextTranslations[canonical][lang];return result?value.replace(trimmed,result):value;};
 document.querySelectorAll('input[placeholder],textarea[placeholder],[aria-label],[title],option').forEach(el=>{
  for(const attr of ['placeholder','aria-label','title']){const value=el.getAttribute(attr);if(value){const next=translate(value);if(next!==value)el.setAttribute(attr,next);}}
  if(el.tagName==='OPTION'){const value=el.textContent,next=translate(value);if(next!==value)el.textContent=next;}
 });
}
const originalSetLanguage=setLanguage;
setLanguage=function(lang){originalSetLanguage(lang);translateSiteAttributes(['fr','en','ht'].includes(lang)?lang:'fr');};
setLanguage((()=>{try{return localStorage.getItem('mrjery_language')||'fr'}catch(e){return 'fr'}})());
document.getElementById('languageButton')?.addEventListener('click',()=>document.getElementById('languageMenu').classList.toggle('show'));
document.querySelectorAll('#languageMenu [data-lang]').forEach(b=>b.addEventListener('click',()=>setLanguage(b.dataset.lang)));
document.getElementById('landingLoginBtn')?.addEventListener('click',()=>openAuth('login'));
document.getElementById('leaveOnlineMatchBtn')?.addEventListener('click',cleanupMatchVoice);
document.getElementById('onlineGameBack')?.addEventListener('click',cleanupMatchVoice);
window.addEventListener('beforeunload',cleanupMatchVoice);
document.getElementById('landingRegisterBtn')?.addEventListener('click',()=>openAuth('register'));
document.getElementById('landingAboutBtn')?.addEventListener('click',()=>showScreen('aboutScreen'));
document.getElementById('landingAboutPill')?.addEventListener('click',()=>showScreen('aboutScreen'));
document.getElementById('landingGameBtn')?.addEventListener('click',()=>showScreen('localScreen'));
document.getElementById('aboutLanguageButton')?.addEventListener('click',()=>{showScreen('landingScreen');document.getElementById('languageMenu')?.classList.add('show');});
document.getElementById('aboutBack')?.addEventListener('click',()=>showScreen('landingScreen'));
document.getElementById('aboutJoinBtn')?.addEventListener('click',()=>openAuth('register'));
document.getElementById('authLoginTab')?.addEventListener('click',()=>setAuthMode('login'));
document.getElementById('authRegisterTab')?.addEventListener('click',()=>setAuthMode('register'));
document.getElementById('goRegisterBtn')?.addEventListener('click',()=>setAuthMode('register'));
document.getElementById('goLoginBtn')?.addEventListener('click',()=>setAuthMode('login'));


/* ==================================================
   CHAT DU MATCH + VOIX WEBRTC
================================================== */
function matchSend(payload){if(socket&&socket.readyState===WebSocket.OPEN)socket.send(JSON.stringify(payload));}
function renderMatchChat(items){
  const box=document.getElementById('matchChatMessages'); if(!box)return;
  const signature=JSON.stringify((items||[]).slice(-80)); if(signature===renderedChatSignature)return; renderedChatSignature=signature;
  box.innerHTML=''; (items||[]).slice(-80).forEach(function(item){
    const row=document.createElement('div');row.className='match-chat-message';
    const name=document.createElement('strong');name.textContent=(item.sender||'Joueur')+': ';
    const msg=document.createElement('span');msg.textContent=item.text||'';
    const time=document.createElement('small');if(item.time){try{time.textContent=new Date(Number(item.time)*1000).toLocaleTimeString([], {hour:'2-digit',minute:'2-digit'});}catch(e){}}
    row.append(name,msg,time);box.appendChild(row);
  }); box.scrollTop=box.scrollHeight;
}
document.getElementById('matchChatForm')?.addEventListener('submit',function(e){e.preventDefault();const input=document.getElementById('matchChatInput');const message=(input?.value||'').trim();if(!message||!onlineRoom)return;if(!socket||socket.readyState!==WebSocket.OPEN){document.getElementById('matchVoiceStatus').textContent='Koneksyon sèvè a pa disponib.';return;}matchSend({type:'chat',room:onlineRoom,message});input.value='';});
document.getElementById('toggleMatchChat')?.addEventListener('click',function(){const body=document.getElementById('matchChatBody');if(!body)return;const hidden=body.style.display==='none';body.style.display=hidden?'':'none';this.textContent=hidden?'Masquer':'Afficher chat';});
function voiceIsSpectator(){return onlineConnectionMode==='spectator'||Number(onlinePlayer||0)===0;}
function voiceSend(to,type,payload){matchSend({type:'voice_signal',room:onlineRoom,to:to,signal_type:type,payload:payload});}
function ensureVoiceJoined(){if(!onlineRoom||!socket||socket.readyState!==WebSocket.OPEN||voiceJoinedRoom===String(onlineRoom))return;voiceJoinedRoom=String(onlineRoom);matchSend({type:'voice_join',room:onlineRoom});}
async function getMatchMic(){if(!matchMicStream){matchMicStream=await navigator.mediaDevices.getUserMedia({audio:{echoCancellation:true,noiseSuppression:true,autoGainControl:true},video:false});}matchMicEnabled=true;matchMicStream.getAudioTracks().forEach(t=>t.enabled=true);return matchMicStream;}
function closeVoicePeer(id){const pc=matchVoicePeers.get(String(id));if(pc){try{pc.close();}catch(e){}matchVoicePeers.delete(String(id));}}
function createVoicePeer(id){id=String(id);let pc=matchVoicePeers.get(id);if(pc)return pc;pc=new RTCPeerConnection({iceServers:[{urls:'stun:stun.l.google.com:19302'},{urls:'stun:stun1.l.google.com:19302'}]});matchVoicePeers.set(id,pc);
  if(matchMicStream&&matchMicEnabled)matchMicStream.getAudioTracks().forEach(track=>pc.addTrack(track,matchMicStream));
  else pc.addTransceiver('audio',{direction:'recvonly'});
  pc.onicecandidate=e=>{if(e.candidate)voiceSend(id,'ice',e.candidate.toJSON());};
  pc.ontrack=e=>{let audio=document.getElementById('voiceAudio_'+id);if(!audio){audio=document.createElement('audio');audio.id='voiceAudio_'+id;audio.autoplay=true;audio.playsInline=true;audio.style.display='none';document.getElementById('matchRemoteAudios')?.appendChild(audio);}if(e.streams&&e.streams[0])audio.srcObject=e.streams[0];audio.muted=voiceMutedPeers.has(id)||(voiceMuteAllSpectators&&voicePeerMeta.get(id)?.role==='spectator');audio.play().catch(()=>{});renderVoicePeerControls();};
  pc.onconnectionstatechange=()=>{if(['failed','closed'].includes(pc.connectionState))closeVoicePeer(id);};return pc;
}
async function handleVoicePeerJoin(data){if(!onlineRoom||String(data.room)!==String(onlineRoom))return;const id=String(data.peer_id);if(!id||id==='undefined')return;voicePeerMeta.set(id,{role:data.role||'player',username:data.username||'Jwè'});renderVoicePeerControls();
  // Moun ki te deja nan chanm nan lanse òf la; nouvo moun nan reponn, konsa yo evite kolizyon.
  try{const pc=createVoicePeer(id);if(matchMicStream&&matchMicEnabled)matchMicStream.getAudioTracks().forEach(track=>{if(!pc.getSenders().some(s=>s.track===track))pc.addTrack(track,matchMicStream);});const offer=await pc.createOffer();await pc.setLocalDescription(offer);voiceSend(id,'description',pc.localDescription.toJSON());}catch(e){console.warn('Voice offer failed',e);}
}
function handleVoicePeerList(peers){(peers||[]).forEach(p=>{const id=String(p.peer_id);voicePeerMeta.set(id,{role:p.role||'player',username:p.username||'Jwè'});});renderVoicePeerControls();}
async function handleVoiceSignal(data){if(String(data.room)!==String(onlineRoom))return;const from=String(data.from_id);if(!from||from==='undefined')return;voicePeerMeta.set(from,{role:data.from_role||'player',username:data.from_username||'Jwè'});renderVoicePeerControls();try{const pc=createVoicePeer(from);const payload=data.payload||{};
  if(data.signal_type==='description'){const desc=new RTCSessionDescription(payload);await pc.setRemoteDescription(desc);if(desc.type==='offer'){const answer=await pc.createAnswer();await pc.setLocalDescription(answer);voiceSend(from,'description',pc.localDescription.toJSON());}}
  else if(data.signal_type==='ice'){try{await pc.addIceCandidate(new RTCIceCandidate(payload));}catch(e){console.debug('ICE candidate ignored',e);}}
}catch(e){console.warn('Voice signal failed',e);}}
document.getElementById('matchMicButton')?.addEventListener('click',async function(){const status=document.getElementById('matchVoiceStatus');try{
  if(matchMicEnabled){matchMicEnabled=false;if(matchMicStream)matchMicStream.getAudioTracks().forEach(t=>t.enabled=false);this.textContent='🎤 Aktive mikwo';status.textContent='Mikwo fèmen';return;}
  if(!navigator.mediaDevices||!navigator.mediaDevices.getUserMedia)throw new Error('Navigatè a pa sipòte mikwo a. Itilize HTTPS.');
  await getMatchMic();this.textContent='🔇 Koupe mikwo';status.textContent='Mikwo aktive';ensureVoiceJoined();
  // Re-negotiate existing connections after microphone permission is granted.
  for(const [id,pc] of matchVoicePeers){if(!pc.getSenders().some(s=>s.track&&s.track.kind==='audio'))matchMicStream.getAudioTracks().forEach(track=>pc.addTrack(track,matchMicStream));const offer=await pc.createOffer();await pc.setLocalDescription(offer);voiceSend(id,'description',pc.localDescription.toJSON());}
}catch(e){status.textContent=e.message||'Pa kapab aktive mikwo a.';}});
function renderVoicePeerControls(){const box=document.getElementById('matchVoicePeerControls');if(!box)return;box.innerHTML='';for(const [id,meta] of voicePeerMeta){const b=document.createElement('button');b.type='button';const muted=voiceMutedPeers.has(id);b.textContent=(muted?'🔊 Ouvri son: ':'🔇 Mute: ')+(meta.username||'Jwè')+(meta.role==='spectator'?' (spektatè)':'');b.addEventListener('click',()=>{if(voiceMutedPeers.has(id))voiceMutedPeers.delete(id);else voiceMutedPeers.add(id);const a=document.getElementById('voiceAudio_'+id);if(a)a.muted=voiceMutedPeers.has(id)||(voiceMuteAllSpectators&&meta.role==='spectator');renderVoicePeerControls();});box.appendChild(b);}}
document.getElementById('muteAllSpectatorsButton')?.addEventListener('click',function(){voiceMuteAllSpectators=!voiceMuteAllSpectators;this.textContent=voiceMuteAllSpectators?'🔊 Tande spektatè yo':'🔇 Mute tout spektatè';for(const [id,meta] of voicePeerMeta){const a=document.getElementById('voiceAudio_'+id);if(a)a.muted=voiceMutedPeers.has(id)||(voiceMuteAllSpectators&&meta.role==='spectator');}});
function cleanupMatchVoice(){if(onlineRoom)matchSend({type:'voice_leave',room:onlineRoom});matchVoicePeers.forEach(pc=>{try{pc.close();}catch(e){}});matchVoicePeers.clear();voicePeerMeta.clear();voiceMutedPeers.clear();document.getElementById('matchRemoteAudios')?.replaceChildren();renderVoicePeerControls();voiceJoinedRoom=null;if(matchMicStream){matchMicStream.getTracks().forEach(t=>t.stop());matchMicStream=null;}matchMicEnabled=false;const a=document.getElementById('matchRemoteAudio');if(a)a.srcObject=null;const b=document.getElementById('matchMicButton');if(b)b.textContent='🎤 Aktive mikwo';const st=document.getElementById('matchVoiceStatus');if(st)st.textContent='Mikwo fèmen';}

// Traduction continue des écrans internes et des éléments créés après le changement de langue.
// Ainsi, Play Online, Spectators et Play with a Friend gardent la langue choisie même après navigation.
Object.assign(fullSiteTextTranslations, {
 'Jouer en ligne':{fr:'Jouer en ligne',en:'Play Online',ht:'Jwe Anliy'},
 'Play Online':{fr:'Jouer en ligne',en:'Play Online',ht:'Jwe Anliy'},
 'Jouer avec un ami':{fr:'Jouer avec un ami',en:'Play with a Friend',ht:'Jwe ak yon zanmi'},
 'Play with a Friend':{fr:'Jouer avec un ami',en:'Play with a Friend',ht:'Jwe ak yon zanmi'},
 'Spectateurs':{fr:'Spectateurs',en:'Spectators',ht:'Espektatè'},
 'Spectators':{fr:'Spectateurs',en:'Spectators',ht:'Espektatè'},
 'Créer une salle':{fr:'Créer une salle',en:'Create a room',ht:'Kreye yon chanm'},
 'Rejoindre une salle':{fr:'Rejoindre une salle',en:'Join a room',ht:'Antre nan yon chanm'},
 'Code de la salle':{fr:'Code de la salle',en:'Room code',ht:'Kòd chanm lan'},
 'Entrer le code':{fr:'Entrer le code',en:'Enter code',ht:'Antre kòd la'},
 'Copier le code':{fr:'Copier le code',en:'Copy code',ht:'Kopye kòd la'},
 'Inviter un ami':{fr:'Inviter un ami',en:'Invite a friend',ht:'Envite yon zanmi'},
 'En attente d’un joueur...':{fr:'En attente d’un joueur...',en:'Waiting for a player...',ht:'Ap tann yon jwè...'},
 'En attente d’un adversaire...':{fr:'En attente d’un adversaire...',en:'Waiting for an opponent...',ht:'Ap tann yon advèsè...'},
 'Aucun match en direct pour le moment.':{fr:'Aucun match en direct pour le moment.',en:'No live matches right now.',ht:'Pa gen match an dirèk pou kounye a.'},
 'Aucun joueur disponible.':{fr:'Aucun joueur disponible.',en:'No players available.',ht:'Pa gen jwè disponib.'},
 'Actualiser la liste':{fr:'Actualiser la liste',en:'Refresh list',ht:'Rafrechi lis la'},
 'Annuler la recherche':{fr:'Annuler la recherche',en:'Cancel search',ht:'Anile rechèch la'},
 'Annuler le défi':{fr:'Annuler le défi',en:'Cancel challenge',ht:'Anile defi a'},
 'Envoyer une invitation':{fr:'Envoyer une invitation',en:'Send invitation',ht:'Voye yon envitasyon'},
 'Accepter le défi':{fr:'Accepter le défi',en:'Accept challenge',ht:'Aksepte defi a'},
 'Refuser le défi':{fr:'Refuser le défi',en:'Decline challenge',ht:'Refize defi a'},
 'Aucun défi disponible.':{fr:'Aucun défi disponible.',en:'No challenges available.',ht:'Pa gen defi disponib.'},
 'Liste des joueurs':{fr:'Liste des joueurs',en:'Player list',ht:'Lis jwè yo'},
 'Joueurs disponibles':{fr:'Joueurs disponibles',en:'Available players',ht:'Jwè ki disponib'},
 'Créer une partie':{fr:'Créer une partie',en:'Create a game',ht:'Kreye yon pati'},
 'Rejoindre une partie':{fr:'Rejoindre une partie',en:'Join a game',ht:'Antre nan yon pati'},
 'Choisir la durée':{fr:'Choisir la durée',en:'Choose duration',ht:'Chwazi dire a'},
 'Temps de jeu':{fr:'Temps de jeu',en:'Game time',ht:'Tan jwèt la'},
 'Retour au tableau de bord':{fr:'Retour au tableau de bord',en:'Back to dashboard',ht:'Retounen nan tablo prensipal la'},
 'Retour au menu':{fr:'Retour au menu',en:'Back to menu',ht:'Retounen nan meni an'},
 'Quitter':{fr:'Quitter',en:'Leave',ht:'Kite'},
 'Envoyer':{fr:'Envoyer',en:'Send',ht:'Voye'},
 'Message':{fr:'Message',en:'Message',ht:'Mesaj'},
 'Écrire un message...':{fr:'Écrire un message...',en:'Write a message...',ht:'Ekri yon mesaj...'},
 'Chargement...':{fr:'Chargement...',en:'Loading...',ht:'Ap chaje...'},
 'Erreur de connexion.':{fr:'Erreur de connexion.',en:'Connection error.',ht:'Erè koneksyon.'},
 'Connexion au serveur...':{fr:'Connexion au serveur...',en:'Connecting to server...',ht:'Ap konekte ak sèvè a...'},
 'Aucun joueur trouvé.':{fr:'Aucun joueur trouvé.',en:'No players found.',ht:'Pa jwenn okenn jwè.'},
 'Match terminé':{fr:'Match terminé',en:'Match finished',ht:'Match la fini'},
 'Victoire':{fr:'Victoire',en:'Victory',ht:'Viktwa'},
 'Défaite':{fr:'Défaite',en:'Defeat',ht:'Defèt'},
 'Égalité':{fr:'Égalité',en:'Draw',ht:'Match nil'},
 'Annuler':{fr:'Annuler',en:'Cancel',ht:'Anile'},
 'Confirmer':{fr:'Confirmer',en:'Confirm',ht:'Konfime'},
 'Fermer':{fr:'Fermer',en:'Close',ht:'Fèmen'},
 'Enregistrer':{fr:'Enregistrer',en:'Save',ht:'Anrejistre'},
 'Rechercher':{fr:'Rechercher',en:'Search',ht:'Chèche'},
 'Aucun résultat.':{fr:'Aucun résultat.',en:'No results.',ht:'Pa gen rezilta.'}
});

// Traductions complémentaires pour tous les écrans internes (jeu en ligne, amis, spectateurs, salle et match).
Object.assign(fullSiteTextTranslations, {
 'Jouer en Ligne':{fr:'Jouer en Ligne',en:'Play Online',ht:'Jwe Anliy'},
 'Trouver un adversaire':{fr:'Trouver un adversaire',en:'Find an opponent',ht:'Chèche yon advèsè'},
 'Jouer avec un ami':{fr:'Jouer avec un ami',en:'Play with a Friend',ht:'Jwe ak yon zanmi'},
 'Salle d’attente':{fr:'Salle d’attente',en:'Waiting Room',ht:'Sal datant'},
 'Salle d\'attente':{fr:'Salle d’attente',en:'Waiting Room',ht:'Sal datant'},
 'Regarder un match':{fr:'Regarder un match',en:'Watch a Match',ht:'Gade yon match'},
 'Recherche d’un adversaire...':{fr:'Recherche d’un adversaire...',en:'Searching for an opponent...',ht:'Ap chèche yon advèsè...'},
 'Recherche d\'un adversaire...':{fr:'Recherche d’un adversaire...',en:'Searching for an opponent...',ht:'Ap chèche yon advèsè...'},
 'Créer une partie':{fr:'Créer une partie',en:'Create a Game',ht:'Kreye yon pati'},
 'Rejoindre une partie':{fr:'Rejoindre une partie',en:'Join a Game',ht:'Antre nan yon pati'},
 'Paramètres de l’invitation':{fr:'Paramètres de l’invitation',en:'Invitation Settings',ht:'Paramèt envitasyon an'},
 'Paramètres de l\'invitation':{fr:'Paramètres de l’invitation',en:'Invitation Settings',ht:'Paramèt envitasyon an'},
 'Durée du match':{fr:'Durée du match',en:'Match Duration',ht:'Dire match la'},
 'minute':{fr:'minute',en:'minute',ht:'minit'}, 'minutes':{fr:'minutes',en:'minutes',ht:'minit'},
 'Gwosè tablo':{fr:'Taille du plateau',en:'Board Size',ht:'Gwosè tablo'},
 'Koulè tablo sou telefòn pa w':{fr:'Couleur du plateau sur votre téléphone',en:'Board color on your phone',ht:'Koulè tablo sou telefòn pa w'},
 'Klasik blan':{fr:'Blanc classique',en:'Classic White',ht:'Blan klasik'},
 'Nuit ble':{fr:'Ble nuit',en:'Midnight Blue',ht:'Ble nuit'},
 'Vèt mant':{fr:'Vert menthe',en:'Mint Green',ht:'Vèt mant'},
 'Woz dous':{fr:'Rose doux',en:'Soft Pink',ht:'Woz dous'},
 'Sab klè':{fr:'Sable clair',en:'Light Sand',ht:'Sab klè'},
 'Joueurs en ligne':{fr:'Joueurs en ligne',en:'Players Online',ht:'Jwè ki anliy'},
 'Chargement des joueurs...':{fr:'Chargement des joueurs...',en:'Loading players...',ht:'Ap chaje jwè yo...'},
 'Code :':{fr:'Code :',en:'Code:',ht:'Kòd:'}, 'Joueur :':{fr:'Joueur :',en:'Player:',ht:'Jwè:'},
 'Retour':{fr:'Retour',en:'Back',ht:'Retounen'},
 'En attente...':{fr:'En attente...',en:'Waiting...',ht:'Ap tann...'},
 'Spectateurs :':{fr:'Spectateurs :',en:'Spectators:',ht:'Espektatè:'},
 'Choisissez un match en direct :':{fr:'Choisissez un match en direct :',en:'Choose a live match:',ht:'Chwazi yon match an dirèk:'},
 'Actualiser':{fr:'Actualiser',en:'Refresh',ht:'Rafrechi'},
 'Gomoku en Ligne':{fr:'Gomoku en Ligne',en:'Online Gomoku',ht:'Gomoku Anliy'},
 'Connexion...':{fr:'Connexion...',en:'Connecting...',ht:'Ap konekte...'},
 'Joueur 1':{fr:'Joueur 1',en:'Player 1',ht:'Jwè 1'}, 'Joueur 2':{fr:'Joueur 2',en:'Player 2',ht:'Jwè 2'},
 'Noir':{fr:'Noir',en:'Black',ht:'Nwa'}, 'Rouge':{fr:'Rouge',en:'Red',ht:'Wouj'},
 'Chat du match':{fr:'Chat du match',en:'Match Chat',ht:'Chat match la'},
 'Masquer':{fr:'Masquer',en:'Hide',ht:'Kache'}, 'Voye':{fr:'Envoyer',en:'Send',ht:'Voye'},
 '🎤 Aktive mikwo':{fr:'🎤 Activer le micro',en:'🎤 Turn Mic On',ht:'🎤 Aktive mikwo'},
 '🔇 Koupe mikwo':{fr:'🔇 Couper le micro',en:'🔇 Turn Mic Off',ht:'🔇 Koupe mikwo'},
 'Mikwo fèmen':{fr:'Micro coupé',en:'Microphone off',ht:'Mikwo fèmen'},
 'Vwa a disponib ant jwè yo.':{fr:'La voix est disponible entre les joueurs.',en:'Voice chat is available between players.',ht:'Vwa a disponib ant jwè yo.'},
 'Spektatè yo ka tande, men yo pa ka pale.':{fr:'Les spectateurs peuvent écouter, mais pas parler.',en:'Spectators can listen but cannot speak.',ht:'Espektatè yo ka tande, men yo pa ka pale.'},
 'Mòd spektatè: ou ka tande, men ou pa ka pale.':{fr:'Mode spectateur : vous pouvez écouter, mais pas parler.',en:'Spectator mode: you can listen, but cannot speak.',ht:'Mòd spektatè: ou ka tande, men ou pa ka pale.'},
 'Nouvelle partie':{fr:'Nouvelle partie',en:'New Game',ht:'Nouvo pati'},
 'Kite match la':{fr:'Quitter le match',en:'Leave Match',ht:'Kite match la'},
 'Retour au menu':{fr:'Retour au menu',en:'Back to Menu',ht:'Retounen nan meni an'},
 'Accepter':{fr:'Accepter',en:'Accept',ht:'Aksepte'}, 'Refuser':{fr:'Refuser',en:'Decline',ht:'Refize'},
 'Déconnexion':{fr:'Déconnexion',en:'Log Out',ht:'Dekonekte'}, 'Déconnecté':{fr:'Déconnecté',en:'Disconnected',ht:'Dekonekte'},
 'En ligne':{fr:'En ligne',en:'Online',ht:'Anliy'}, 'Hors ligne':{fr:'Hors ligne',en:'Offline',ht:'Pa anliy'},
 'Aucun match disponible.':{fr:'Aucun match disponible.',en:'No matches available.',ht:'Pa gen match disponib.'},
 'Aucun match en direct.':{fr:'Aucun match en direct.',en:'No live matches.',ht:'Pa gen match an dirèk.'},
 'Le match est terminé.':{fr:'Le match est terminé.',en:'The match is over.',ht:'Match la fini.'},
 'Impossible de se connecter au serveur.':{fr:'Impossible de se connecter au serveur.',en:'Unable to connect to the server.',ht:'Pa kapab konekte ak sèvè a.'},
 'Code de salle invalide.':{fr:'Code de salle invalide.',en:'Invalid room code.',ht:'Kòd chanm lan pa valab.'},
 'Veuillez entrer un code de salle.':{fr:'Veuillez entrer un code de salle.',en:'Please enter a room code.',ht:'Tanpri antre kòd chanm lan.'},
 'Votre invitation a été envoyée.':{fr:'Votre invitation a été envoyée.',en:'Your invitation has been sent.',ht:'Yo voye envitasyon ou an.'},
 'Invitation envoyée':{fr:'Invitation envoyée',en:'Invitation Sent',ht:'Yo voye envitasyon an'},
 'Annuler la partie':{fr:'Annuler la partie',en:'Cancel Game',ht:'Anile pati a'},
 'Rechercher un joueur':{fr:'Rechercher un joueur',en:'Search for a Player',ht:'Chèche yon jwè'},
 'Nom du joueur':{fr:'Nom du joueur',en:'Player Name',ht:'Non jwè a'},
 'Pseudo':{fr:'Pseudo',en:'Username',ht:'Psedonim'},
 'Créer':{fr:'Créer',en:'Create',ht:'Kreye'}, 'Rejoindre':{fr:'Rejoindre',en:'Join',ht:'Antre'},
 'Prêt':{fr:'Prêt',en:'Ready',ht:'Pare'}, 'En attente d’un joueur...':{fr:'En attente d’un joueur...',en:'Waiting for a player...',ht:'Ap tann yon jwè...'},
 'En attente d’un adversaire...':{fr:'En attente d’un adversaire...',en:'Waiting for an opponent...',ht:'Ap tann yon advèsè...'},
 'Aucune partie disponible.':{fr:'Aucune partie disponible.',en:'No games available.',ht:'Pa gen pati disponib.'},
 'Votre tour':{fr:'Votre tour',en:'Your turn',ht:'Se tou pa w'}, 'Tour de l’adversaire':{fr:'Tour de l’adversaire',en:'Opponent’s turn',ht:'Se tou advèsè a'},
 'Victoire !':{fr:'Victoire !',en:'You Win!',ht:'Ou genyen!'}, 'Vous avez perdu.':{fr:'Vous avez perdu.',en:'You lost.',ht:'Ou pèdi.'},
 'Match nul':{fr:'Match nul',en:'Draw',ht:'Match nil'},
 'Fermer':{fr:'Fermer',en:'Close',ht:'Fèmen'}, 'Envoyer':{fr:'Envoyer',en:'Send',ht:'Voye'},
 'Annuler':{fr:'Annuler',en:'Cancel',ht:'Anile'}, 'Confirmer':{fr:'Confirmer',en:'Confirm',ht:'Konfime'}
});

function translateCurrentLanguageAttributes(lang){
  const map=fullSiteTextTranslations;
  const translate=value=>{
    if(!value)return value;
    const trim=value.trim(); let key=map[trim]?trim:Object.keys(map).find(k=>Object.values(map[k]).includes(trim));
    return key&&map[key][lang]?value.replace(trim,map[key][lang]):value;
  };
  document.querySelectorAll('input[placeholder],textarea[placeholder],[title],[aria-label]').forEach(el=>{
    for(const attr of ['placeholder','title','aria-label']) if(el.hasAttribute(attr)) el.setAttribute(attr,translate(el.getAttribute(attr)));
  });
  document.querySelectorAll('option').forEach(el=>{const t=translate(el.textContent);if(t!==el.textContent)el.textContent=t;});
}
let __mrjeryTranslationTimer=null;
const __mrjeryLanguageObserver=new MutationObserver(()=>{
  if(__mrjeryTranslationTimer)clearTimeout(__mrjeryTranslationTimer);
  __mrjeryTranslationTimer=setTimeout(()=>{
    const lang=(localStorage.getItem('mrjery_language')||'fr');
    if(['fr','en','ht'].includes(lang)){translateWholeSiteText(lang);translateCurrentLanguageAttributes(lang);}
  },40);
});
__mrjeryLanguageObserver.observe(document.body,{subtree:true,childList:true,characterData:true});
try { const __lang=localStorage.getItem('mrjery_language')||'fr'; translateWholeSiteText(__lang); translateCurrentLanguageAttributes(__lang); } catch(e) {}

// Le compte reste mémorisé dans localStorage et est restauré au démarrage.
// Un incident réseau ne supprime jamais la session; seul le bouton Déconnexion l'efface.
// Au chargement, tenter de restaurer le compte sauvegardé sans exiger une nouvelle connexion.
(function restoreSavedAccountAtStartup(){
  let token = null;
  try { token = localStorage.getItem("mrjery_account_token"); } catch(e) {}
  if (!token) return;
  try {
    connectServer(function(){
      if (accountConnected) { updateAccountDisplay(); refreshDashboardUser(); }
    });
  } catch(e) { console.warn("Restauration de session reportée", e); }
})();
</script>

</body>
</html>
