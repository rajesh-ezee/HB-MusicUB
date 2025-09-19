import os

from ... import *
from pyrogram import filters


@app.on_message(cdz(["paken", "hm", "wow", "super", "wait", "ham", "👀👀"])
    & filters.private & filters.me)
async def self_media(client, message):
    try:
        replied = message.reply_to_message
        if not replied:
            return
        if not (replied.photo or replied.video):
            return
        location = await client.download_media(replied)
        await client.send_document("me", location)
        os.remove(location)
    except Exception as e:
        print("Error: `{e}`")
        return


add_command_help(
    "self-destruct",
    [
        [".hb", "save one time pic"],
        ["!hb", "Save Self Desitruct Without Download"],
    ],
)