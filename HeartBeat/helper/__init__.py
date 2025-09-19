import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "HeartBeat"])

async def join(client):
    try:
        await client.join_chat("HeartBeat_Fam")
    except BaseException:
        pass
