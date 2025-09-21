from pyrogram import filters, Client
import asyncio
from pyrogram.types import Message
from pyrogram.methods import messages
from HeartBeat.database.pmpermitdb import get_approved_users, pm_guard
import HeartBeat.database.pmpermitdb as HeartBeat
from config import LOG_GROUP, PM_LOGGER

FLOOD_CTRL = 0
ALLOWED = []
USERS_AND_WARNS = {}

# Default PM Permit Image
HeartBeat.PMPERMIT_IMAGE = "https://files.catbox.moe/r5hiwl.jpg"  # Replace with your own image link


async def denied_users(filter, client: Client, message: Message):
    if not await pm_guard():
        return False
    if message.chat.id in (await get_approved_users()):
        return False
    else:
        return True


def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


@Client.on_message(filters.command("xsetlimit", ["."]) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**Set limit to what?**")
        return
    await HeartBeat.set_limit(int(arg))
    await message.edit(f"**Limit set to {arg}**")


@Client.on_message(filters.command("xsetblockmsg", ["."]) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**What message to set**")
        return
    if arg == "default":
        await HeartBeat.set_block_message(HeartBeat.BLOCKED)
        await message.edit("**Block message set to default**.")
        return
    await HeartBeat.set_block_message(f"`{arg}`")
    await message.edit("**Custom block message set**")


@Client.on_message(filters.command(["allow", "ap", "approve", "a"], ["."]) & filters.me & filters.private)
async def allow(client, message):
    chat_id = message.chat.id
    pmpermit, pm_message, limit, block_message = await HeartBeat.get_pm_settings()
    await HeartBeat.allow_user(chat_id)
    await message.edit(f"**I have allowed [you](tg://user?id={chat_id}) to PM me.**")
    async for message in client.search_messages(
        chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
    ):
        await message.delete()
    USERS_AND_WARNS.update({chat_id: 0})


@Client.on_message(filters.command(["deny", "dap", "disapprove", "da"], ["."]) & filters.me & filters.private)
async def deny(client, message):
    chat_id = message.chat.id
    await HeartBeat.deny_user(chat_id)
    await message.edit(f"**I have denied [you](tg://user?id={chat_id}) to PM me.**")


# 🔹 New Command: Set PM Image
@Client.on_message(filters.command("xsetpmimg", ["."]) & filters.me)
async def set_pm_image(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.edit("**Reply to an image with `.setpmimg` to set it as PM Permit image.**")
        return
    photo = message.reply_to_message.photo.file_id
    HeartBeat.PMPERMIT_IMAGE = photo
    await message.edit("✅ **PM Permit image has been updated.**")


@Client.on_message(
    filters.private
    & filters.create(denied_users)
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
)
async def reply_pm(app: Client, message):
    global FLOOD_CTRL
    pmpermit, pm_message, limit, block_message = await HeartBeat.get_pm_settings()
    user = message.from_user.id
    user_warns = 0 if user not in USERS_AND_WARNS else USERS_AND_WARNS[user]

    if PM_LOGGER:
        await app.send_message(PM_LOGGER, f"{message.text}")

    if user_warns <= limit - 2:
        user_warns += 1
        USERS_AND_WARNS.update({user: user_warns})
        if not FLOOD_CTRL > 0:
            FLOOD_CTRL += 1
        else:
            FLOOD_CTRL = 0
            return

        async for msg in app.search_messages(
            chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
        ):
            await msg.delete()

        
You said:
warn(PMPERMIT_MESSAGE) message doesnot displayed/working.

from HeartBeat.database import cli
import asyncio

collection = cli["HeartBeat"]["pmpermit"]

# Default PM Permit message
PMPERMIT_MESSAGE = (
    "<blockquote>☆ . * ● ¸ . ✦ .★° :. ★ * • ○ ° ★</blockquote>\n"
    "<blockquote>ʜᴇʏ, ɪ'ᴍ 𝐇𝐞𝐚𝐫𝐭𝐁𝐞𝐚𝐭-✗-𝐁𝐨𝐭</blockquote>\n"
    "<blockquote>➽───────────────❥</blockquote>\n"
    "<blockquote>💕 ᴛᴀɢ ᴍʏ ʟᴏᴠᴇ 🦋  \n"
    "🔗 https://t.me/HeartBeat_Fam</blockquote>\n"
    "<blockquote>➽───────────────❥</blockquote>\n"
    "<blockquote>😈 ᴏᴛʜᴇʀᴡɪꜱᴇ, ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴍʏ ʙᴏꜱꜱ ᴄᴏᴍᴇꜱ.  \n"
    "🚫 ᴅᴏɴ'ᴛ ꜱᴘᴀᴍ ᴍᴇ – ʏᴏᴜ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ʙʟᴏᴄᴋᴇᴅ (ᴜᴘ ᴛᴏ 3 ᴡᴀʀɴɪɴɢꜱ).</blockquote>\n"
    "<blockquote>☆ . * ● ¸ . ✦ .★° :. ★ * • ○ ° ★</blockquote>"
)

# Default block message
BLOCKED = (
    "<blockquote>ʙᴇᴇᴘ ʙᴏᴏᴘ ⚠️ ꜰᴏᴜɴᴅ ᴀ ꜱᴘᴀᴍᴍᴇʀ!, "
    "ʙʟᴏᴄᴋᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 🚫</blockquote>"
)

# Default warn limit
LIMIT = 3


# Enable / Disable PM Guard
async def set_pm(value: bool):
    doc = {"_id": 1, "pmpermit": value}
    doc2 = {"_id": "Approved", "users": []}
    r = await collection.find_one({"_id": 1})
    r2 = await collection.find_one({"_id": "Approved"})
    if r:
        await collection.update_one({"_id": 1}, {"$set": {"pmpermit": value}})
    else:
        # 🚀 Default ON
        await collection.insert_one({"_id": 1, "pmpermit": True})
    if not r2:
        await collection.insert_one(doc2)


# Set custom anti-pm message
async def set_permit_message(text):
    await collection.update_one({"_id": 1}, {"$set": {"pmpermit_message": text}})


# Set custom block message
async def set_block_message(text):
    await collection.update_one({"_id": 1}, {"$set": {"block_message": text}})


# Set warn limit
async def set_limit(limit):
    await collection.update_one({"_id": 1}, {"$set": {"limit": limit}})


# Get PM settings
async def get_pm_settings():
    result = await collection.find_one({"_id": 1})
    if not result:
        return False
    pmpermit = result.get("pmpermit", True)  # 🚀 default True
    pm_message = result.get("pmpermit_message", PMPERMIT_MESSAGE)
    block_message = result.get("block_message", BLOCKED)
    limit = result.get("limit", LIMIT)
    return pmpermit, pm_message, limit, block_message


# Approve a user
async def allow_user(chat):
    doc = {"_id": "Approved", "users": [chat]}
    r = await collection.find_one({"_id": "Approved"})
    if r:
        await collection.update_one({"_id": "Approved"}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)


# Get approved users
async def get_approved_users():
    results = await collection.find_one({"_id": "Approved"})
    if results:
        return results["users"]
    else:
        return []


# Deny a user
async def deny_user(chat):
    await collection.update_one({"_id": "Approved"}, {"$pull": {"users": chat}})


# Check if PM Guard is active
async def pm_guard():
    result = await collection.find_one({"_id": 1})
    if not result:
        return True  # 🚀 Default ON
    if not result.get("pmpermit", True):
        return False
    else:
        return True

PMGUARD.py
from pyrogram import filters, Client
import asyncio
from pyrogram.types import Message
from pyrogram.methods import messages
from HeartBeat.database.pmpermitdb import get_approved_users, pm_guard
import HeartBeat.database.pmpermitdb as HeartBeat
from config import LOG_GROUP, PM_LOGGER

FLOOD_CTRL = 0
ALLOWED = []
USERS_AND_WARNS = {}

# Default PM Permit Image
HeartBeat.PMPERMIT_IMAGE = "https://files.catbox.moe/r5hiwl.jpg"  # Replace with your own image link


async def denied_users(filter, client: Client, message: Message):
    if not await pm_guard():
        return False
    if message.chat.id in (await get_approved_users()):
        return False
    else:
        return True


def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


@Client.on_message(filters.command("xsetlimit", ["."]) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**Set limit to what?**")
        return
    await HeartBeat.set_limit(int(arg))
    await message.edit(f"**Limit set to {arg}**")


@Client.on_message(filters.command("xsetblockmsg", ["."]) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**What message to set**")
        return
    if arg == "default":
        await HeartBeat.set_block_message(HeartBeat.BLOCKED)
        await message.edit("**Block message set to default**.")
        return
    await HeartBeat.set_block_message(f"{arg}")
    await message.edit("**Custom block message set**")


@Client.on_message(filters.command(["allow", "ap", "approve", "a"], ["."]) & filters.me & filters.private)
async def allow(client, message):
    chat_id = message.chat.id
    pmpermit, pm_message, limit, block_message = await HeartBeat.get_pm_settings()
    await HeartBeat.allow_user(chat_id)
    await message.edit(f"**I have allowed [you](tg://user?id={chat_id}) to PM me.**")
    async for message in client.search_messages(
        chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
    ):
        await message.delete()
    USERS_AND_WARNS.update({chat_id: 0})


@Client.on_message(filters.command(["deny", "dap", "disapprove", "da"], ["."]) & filters.me & filters.private)
async def deny(client, message):
    chat_id = message.chat.id
    await HeartBeat.deny_user(chat_id)
    await message.edit(f"**I have denied [you](tg://user?id={chat_id}) to PM me.**")


# 🔹 New Command: Set PM Image
@Client.on_message(filters.command("xsetpmimg", ["."]) & filters.me)
async def set_pm_image(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.edit("**Reply to an image with .setpmimg to set it as PM Permit image.**")
        return
    photo = message.reply_to_message.photo.file_id
    HeartBeat.PMPERMIT_IMAGE = photo
    await message.edit("✅ **PM Permit image has been updated.**")


@Client.on_message(
    filters.private
    & filters.create(denied_users)
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
)
async def reply_pm(app: Client, message):
    global FLOOD_CTRL
    pmpermit, pm_message, limit, block_message = await HeartBeat.get_pm_settings()
    user = message.from_user.id
    user_warns = 0 if user not in USERS_AND_WARNS else USERS_AND_WARNS[user]

    if PM_LOGGER:
        await app.send_message(PM_LOGGER, f"{message.text}")

    if user_warns <= limit - 2:
        user_warns += 1
        USERS_AND_WARNS.update({user: user_warns})
        if not FLOOD_CTRL > 0:
            FLOOD_CTRL += 1
        else:
            FLOOD_CTRL = 0
            return

        async for msg in app.search_messages(
            chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
        ):
            await msg.delete()

        # 🚀 Send image + text + warning count
        caption_text = f"{pm_message}\n\n⚠️ **𝐖ʌʀиɪиɢ {user_warns}/{limit}**"
        try:
            await app.send_photo(
                chat_id=message.chat.id,
                photo=HeartBeat.PMPERMIT_IMAGE,
                caption=caption_text,
            )
        except Exception:
            # fallback if photo is invalid
            await message.reply(caption_text, disable_web_page_preview=True)
        return

    # If limit exceeded → block
    await message.reply(block_message, disable_web_page_preview=True)
    await app.block_user(message.chat.id)
    USERS_AND_WARNS.update({user: 0})

APMGUARD.py
from pyrogram import filters, Client
import asyncio
from HeartBeat import SUDO_USER
from HeartBeat.modules.help import *
from pyrogram.methods import messages
from .pmguard import get_arg, denied_users

import HeartBeat.database.pmpermitdb as HeartBeat



@Client.on_message(filters.command("pmguard", ["."]) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**I only understand on or off**")
        return
    if arg == "off":
        await HeartBeat.set_pm(False)
        await message.edit("**PM Guard Deactivated**")
    if arg == "on":
        await HeartBeat.set_pm(True)
        await message.edit("**PM Guard Activated**")
@Client.on_message(filters.command("xsetpmmsg", ["."]) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**What message to set**")
        return
    if arg == "default":
        await HeartBeat.set_permit_message(HeartBeat.PMPERMIT_MESSAGE)
        await message.edit("**Anti_PM message set to default**.")
        return
    await HeartBeat.set_permit_message(f"{arg}")
    await message.edit("**Custom anti-pm message set**")


add_command_help(
    "antipm",
    [
        [".pmguard [on or off]", " -> Activates or deactivates anti-pm."],
        [".setpmmsg [message or default]", " -> Sets a custom anti-pm message."],
        [".setblockmsg [message or default]", "-> Sets custom block message."],
        [".setlimit [value]", " -> This one sets a max. message limit for unwanted PMs and when they go beyond it, bamm!."],
        [".allow", " -> Allows a user to PM you."],
        [".deny", " -> Denies a user to PM you."],
    ],
)
ChatGPT said:
Got it 👍

I checked through your pmpermitdb.py, pmguard.py, and apmguard.py.
The reason your PMPERMIT_MESSAGE is not displaying in warn() flow is because of how you’re sending the message in reply_pm.

Here are the issues I see:

1. You’re using app.search_messages(..., query=pm_message, ...)
async for msg in app.search_messages(
    chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
):
    await msg.delete()
🚨 Problem:

query=pm_message is the full formatted blockquote text, not a plain string.

Telegram doesn’t index formatted text for search → so it will never match, meaning nothing gets deleted.

✅ Fix:
Instead of searching with query=pm_message, just delete your last bot message to that user.

2. You are editing the database correctly, but in reply_pm you send:
caption_text = f"{pm_message}\n\n⚠️ **𝐖ʌʀиɪиɢ {user_warns}/{limit}**"
await app.send_photo(chat_id=message.chat.id, photo=HeartBeat.PMPERMIT_IMAGE, caption=caption_text)
If pm_message is stored as code-formatted string (`msg`) in .setpmmsg, then Telegram will display it literally with backticks, not parsed as Markdown/HTML.

✅ Final Fix (Key Changes)
Update reply_pm like this:

@Client.on_message(
    filters.private
    & filters.create(denied_users)
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
)
async def reply_pm(app: Client, message):
    global FLOOD_CTRL
    pmpermit, pm_message, limit, block_message = await HeartBeat.get_pm_settings()
    user = message.from_user.id
    user_warns = USERS_AND_WARNS.get(user, 0)

    if PM_LOGGER:
        await app.send_message(PM_LOGGER, f"PM from {message.from_user.id}: {message.text}")

    if user_warns < limit:
        user_warns += 1
        USERS_AND_WARNS[user] = user_warns

        if FLOOD_CTRL == 0:
            FLOOD_CTRL = 1
        else:
            FLOOD_CTRL = 0
            return

        # 🚀 Always delete your last PM guard message (instead of search by query)
        async for msg in app.get_chat_history(message.chat.id, limit=1):
            if msg.from_user and msg.from_user.is_self:
                await msg.delete()

        # 🚀 Send image + text + warning count
        caption_text = (
            f"{pm_message}\n\n"
            f"⚠️ **𝐖ʌʀиɪиɢ {user_warns}/{limit}**"
        )
        try:
            await app.send_photo(
                chat_id=message.chat.id,
                photo=HeartBeat.PMPERMIT_IMAGE,
                caption=caption_text,
                parse_mode="html",   # 👈 Force HTML parse for blockquote
            )
        except Exception as e:
            await message.reply(
                caption_text,
                disable_web_page_preview=True,
                parse_mode="html"
            )
        return

    # If limit exceeded → block
    await message.reply(block_message, disable_web_page_preview=True)
    await app.block_user(message.chat.id)
    USERS_AND_WARNS.update({user: 0})
