from asyncio import sleep
import random

from pyrogram import Client, filters
from pyrogram.types import Message

from HeartBeat.modules.help import add_command_help

spam_chats = []

# Some random quotes pool
RANDOM_QUOTES = [
    "⚡ Stay strong, the weekend is coming!",
    "🔥 Work hard, dream big!",
    "🌟 Believe you can and you're halfway there.",
    "💫 Keep going, you're doing great!",
    "🚀 Sky is not the limit, it's just the beginning.",
    "✨ Good vibes only!",
    "🌈 Happiness looks good on you.",
    "🌻 Be the reason someone smiles today.",
    "🍀 Luck is what happens when preparation meets opportunity.",
    "🌙 Even the darkest night will end and the sun will rise.",
]


def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


@Client.on_message(filters.command("tagall", ".") & filters.me)
async def mentionall(client: Client, message: Message):
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)

    # If no reply and no text, choose a random quote
    if not direp and not args:
        args = random.choice(RANDOM_QUOTES)

    if not direp and not args:
        return await message.edit("**Send me a message or reply to a message!**")

    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""

    async for usr in client.get_chat_members(chat_id):
        if chat_id not in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 1:
            if args:
                txt = f"<blockquote>{args}</blockquote>\n<blockquote>✰| {usrtxt}</blockquote>"
                await client.send_message(chat_id, txt)
            elif direp:
                await direp.reply(usrtxt)
            await sleep(2)
            usrnum = 0
            usrtxt = ""

    try:
        spam_chats.remove(chat_id)
    except:
        pass


@Client.on_message(filters.command("cancel", ".") & filters.me)
async def cancel_spam(client: Client, message: Message):
    if message.chat.id not in spam_chats:
        return await message.edit("**It seems there is no tagall here.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.edit("**Cancelled.**")


add_command_help(
    "tagall",
    [
        [
            "tagall [text/reply ke chat]",
            "Tag all the members one by one. If no text/reply is given, a random quote will be used.",
        ],
        [
            "cancel",
            "to stop .tagall",
        ],
    ],
)
