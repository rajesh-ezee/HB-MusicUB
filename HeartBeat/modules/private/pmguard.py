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
        caption_text = (
            f"{pm_message}\n\n"
            f"⚠️ **Warning {user_warns}/{limit}**"
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
