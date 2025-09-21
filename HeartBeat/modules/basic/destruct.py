import os

from ... import *
from pyrogram import filters


@Client.on_message(filters.command(["mm", "ait", "am", "👀", "beat", " Beat"], ["h", "w", "H", "W", "👀", "Heart", "heart", ""])
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
