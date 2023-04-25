import asyncio
import disnake as discord
import datetime
import os
import websockets
import uvicorn
import asyncproc
import fastapi
import websockets.server as wsserver
import json
import logging
import main, db
from main import bot

defaulttoken = "umbreon's head"
token = defaulttoken

app = fastapi.FastAPI()

# :O
@app.get("/jd/allcases")
def getallcases():
    return {"Hello": "World"}

async def handler(websocket: wsserver.WebSocketServerProtocol):
    await websocket.send(json.dumps({
        "status": "loading",
        "database_available": isinstance(db.connection, db.sqlite3.Connection),
        "bot_available": bot.is_ready()
    }))
    if bot.is_ready() == True:
        botinfo = {
            "username": bot.user.name,
            "discriminator": bot.user.discriminator,
            "id": bot.user.id
        }
        match bot.status:
            case discord.Status.online:
                botinfo["status"] = "online"
            case discord.Status.idle:
                botinfo["status"] = "idle"
            case discord.Status.dnd:
                botinfo["status"] = "dnd"
            case discord.Status.do_not_disturb:
                botinfo["status"] = "dnd"
            case discord.Status.offline:
                botinfo["status"] = "offline"
            case _:
                botinfo["status"] = "unknown"
        with open("current.log", "r") as file:
            botinfo["output"] = file.read()
        await websocket.send(json.dumps(botinfo))
    while True:
        data = await websocket.recv()
        if isinstance(data, str):
            data = json.loads(data)
            match data["command"]:
                case "start":
                    
                    delay = 0
                    if data["delay"].isnumeric() == True:
                        delay = float(data["delay"])
                    if delay > 0:
                        await asyncio.sleep(delay)
                    asyncio.create_task(bot.start(token))
                    await websocket.send(json.dumps({
                        "status": "success",
                        "delay": delay
                    }))

async def startwebsocket():
    async with wsserver.serve(handler, "localhost", 8000):
        while True:
            await asyncio.sleep(500)

async def multiple_tasks():
    proc = asyncproc.Process("uvicorn launch:app --port 2052")
    input_coroutines = [startwebsocket()] # bot.start(defaulttoken)
    res = await asyncio.gather(*input_coroutines, return_exceptions=True)
    return res

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(multiple_tasks())
