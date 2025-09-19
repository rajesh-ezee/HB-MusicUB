from HeartBeat import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "<blockquote>❍ ɪ ʌᴍ 𝙃𝙀𝘼𝙍𝙏𝘽𝙀𝘼𝙏 ᵘˢᵉʳᵇᵒᵗ \n •───────────────────•</blockquote> \n <blockquote>❖ ᴛʜɪs ᴜʀ ᴄʟᴏɴᴇ ʌssɪsᴛʌɴᴛ \n❖ ᴘᴍ sᴇᴄᴜꝛɪᴛʏ (ᴡᴀꝛɴ | ʙʟᴏᴄᴋ) \n❖ ᴀғᴋ ғᴇʌᴛᴜꝛᴇ (ᴘᴍ & ɢꝛᴏᴜᴘ) \n❖ ᴍᴜsɪᴄ, ᴘʟʌʏ sᴏɴɢs ᴡɪᴛʜ ᴜʀ ᴏᴡɴ ɪᴅ(ɴᴏ ɴᴇᴇᴅ ᴍᴜsɪᴄ-ʙᴏᴛ) \n❖ ᴛʌɢ-ᴀʟʟ, ᴍᴇɴᴛɪᴏɴ ʌɴᴅ ʌᴜᴛᴏ-ꝛᴇᴘʟʏ ǫᴜᴏᴛᴇs ʀʌɪᴅ(ᴛʌɢ ᴡɪᴛʜ ʏᴏᴜꝛ ᴏᴡɴ ɪᴅ) \n❖ ᴄʜᴇᴄᴋ ɴʌᴍᴇ ʜɪsᴛᴏꝛʏ(ɴᴏ ɴᴇᴇᴅ sᴀɴɢ-ᴍʌᴛʌ) \n❖ sᴛʀɪᴄᴋᴇꝛ ᴋʌɴɢ(ᴍʌᴋᴇ sᴛɪᴄᴋᴇʀ) \n❖ ɢʙʌɴ,ɢᴍᴜᴛᴇ & ɪɴғᴏ(ɴᴏ ɴᴇᴇᴅ ʀᴏsᴇ-ʙᴏᴛ) \n❖ ғᴜɴ-ɢʌᴍᴇ ᴡɪᴛʜ ᴍᴏꝛᴇ ғᴇʌᴛᴜꝛᴇs</blockquote> \n <blockquote>❖ /ᴄʟᴏɴᴇ ʏᴏᴜꝛ sᴛʀɪɴɢ sᴇssɪᴏɴ</blockquote> \n<blockquote>\n•───────────────────•\nᴇxᴄʟᴜsɪᴠᴇ ғᴇʌᴛᴜꝛᴇ: \n 𝐒ʌᴠᴇ 𝐒ᴇʟғ 𝐃ɪsᴛꝛᴜᴄᴛ 𝐈ᴍʌɢᴇ \n (𝙊ɴᴇ-ᴛɪᴍᴇ 𝙑ɪᴇᴡ 𝙋ɪᴄ)\n•───────────────────•</blockquote>"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("⌯ ғσʋиᴅᴇя ⌯", url="t.me/GhosttBatt"),
            ],
            [
                InlineKeyboardButton("⌯ ᴄʜʌииᴇʟ ⌯", url="t.me/HeartBeat_Offi"),
            #],
           # [
                InlineKeyboardButton("⌯ ƨʋᴘᴘσят ⌯", url="t.me/HeartBeat_Fam"),
            ],
            [
                InlineKeyboardButton("⌯ ƨяιвɢɢɛи ⌯", url="t.me/HeartBeat_Offi/13"),
                InlineKeyboardButton("⌯ ʌʟʟ ʙσтƨ ⌯", url="https://t.me/HeartBeat_Offi/13"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

# © By itzshukla Your motherfucker if uh Don't gives credits.
@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("ᴡᴀɪᴛ ʙᴀʙʏ ғᴇᴡ sᴇᴄᴏɴᴅs...💌")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="HeartBeat/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f" ᴊᴀ ᴘᴇʟ ᴅᴇ sᴀʙᴋᴏ ᴀʙ ʜʙ-ꜰᴀᴍ ᴋᴏ ʙᴏʟ ᴋᴇ ᴊᴀɴᴀ 🥵 {user.first_name} 💨.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
