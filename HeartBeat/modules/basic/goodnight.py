from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message
import random

from HeartBeat.modules.help import add_command_help

spam_chats = []

# Pool of good morning quotes
RANDOM_QUOTES = [
"🌙 Good night! May your dreams be filled with happiness and love. 🌟",
"💤 Sleep well and wake up refreshed for a brand new day! 🌌",
"🌠 Sweet dreams! Let the stars guide you to peace and joy. ✨",
"🌜 Good night! Rest your mind and let your heart be calm. 💖",
"🌌 May your night be cozy, warm, and full of sweet dreams. 🌙",
"💫 Sleep tight! Tomorrow is a new chance to shine bright. 🌟",
"🌙 Good night! May angels watch over you while you sleep. 😇",
"💤 Rest well! Let your worries fade and happiness stay. 🌌",
"🌠 Sweet dreams! May you drift into a world of magic. ✨",
"🌜 Good night! May your sleep be peaceful and refreshing. 💖",
"🌌 Sleep well! The stars are shining just for you tonight. 🌟",
"💫 Good night! Dream big and let your heart soar high. 🌙",
"🌙 Sweet dreams! May your soul be calm and relaxed. 💖",
"💤 Good night! Let the moonlight guide your peaceful sleep. 🌌",
"🌠 Sleep tight! Tomorrow is waiting for your smile. ✨",
"🌜 Good night! Rest deeply and wake up energized. 🌟",
"🌌 Sweet dreams! May you find joy in every corner of sleep. 💫",
"💫 Sleep well! Let go of the day and embrace the night. 🌙",
"🌙 Good night! May your dreams be filled with magic and love. 💖",
"💤 Sleep tight! Tomorrow holds endless possibilities. 🌌",
"🌠 Good night! Let the stars sprinkle peace on your soul. ✨",
"🌜 Sweet dreams! Rest easy and wake up happy. 🌟",
"🌌 Sleep well! May your heart be light and your mind calm. 💫",
"💫 Good night! Close your eyes and let serenity embrace you. 🌙",
"🌙 Sweet dreams! Let the night fill you with hope. 💖",
"💤 Sleep tight! Tomorrow is a canvas, paint it bright. 🌌",
"🌠 Good night! May you wake up with a smile. ✨",
"🌜 Sleep well! The night whispers peace to your heart. 🌟",
"🌌 Sweet dreams! Let tranquility surround you. 💫",
"💫 Good night! May stars light up your dreams. 🌙",
"🌙 Sleep tight! Let the universe bless your sleep. 💖",
"💤 Good night! Rest, relax, and rejuvenate. 🌌",
"🌠 Sweet dreams! Tomorrow is full of hope and joy. ✨",
"🌜 Sleep well! Let your heart drift into serenity. 🌟",
"🌌 Good night! May your dreams be soft and gentle. 💫",
"💫 Sweet dreams! Sleep with peace and wake with joy. 🌙",
"🌙 Good night! Let your worries dissolve into the night. 💖",
"💤 Sleep tight! May your night be magical and serene. 🌌",
"🌠 Good night! Drift into dreams with happiness. ✨",
"🌜 Sleep well! Let moonlight calm your mind. 🌟",
"🌌 Sweet dreams! May your night be peaceful and lovely. 💫",
"💫 Good night! Rest your body, mind, and soul. 🌙",
"🌙 Sleep tight! Tomorrow is another day to shine. 💖",
"💤 Good night! May your dreams be full of hope. 🌌",
"🌠 Sweet dreams! Let your heart be light tonight. ✨",
"🌜 Sleep well! The night embraces you with calm. 🌟",
"🌌 Good night! May your sleep be deep and restorative. 💫",
"💫 Sweet dreams! Let happiness fill your night. 🌙",
"🌙 Sleep tight! Tomorrow is a fresh new start. 💖",
"💤 Good night! Relax and let go of today’s stress. 🌌",
"🌠 Sweet dreams! May the stars bring you peace. ✨",
"🌜 Sleep well! Let your heart and soul recharge. 🌟",
"🌌 Good night! May your night be full of blessings. 💫",
"💫 Sleep tight! Dream big and wake inspired. 🌙",
"🌙 Sweet dreams! Rest well and feel renewed. 💖",
"💤 Good night! Let the night heal and refresh you. 🌌",
"🌠 Sleep well! The moon is watching over you. ✨",
"🌜 Good night! May your dreams be gentle and happy. 🌟",
"🌌 Sweet dreams! Relax and enjoy the quiet night. 💫",
"💫 Sleep tight! Tomorrow is full of new opportunities. 🌙",
"🌙 Good night! Let peace fill your heart and mind. 💖",
"💤 Sweet dreams! May your sleep be calm and serene. 🌌",
"🌠 Sleep well! Let the night bring you clarity and joy. ✨",
"🌜 Good night! Rest deeply and dream sweetly. 🌟",
"🌌 Sweet dreams! Let happiness surround your sleep. 💫",
"💫 Good night! May the stars guide you to serenity. 🌙",
"🌙 Sleep tight! Let love and peace embrace you tonight. 💖",
"💤 Good night! Drift into dreams full of wonder. 🌌",
"🌠 Sweet dreams! Relax and enjoy the night’s beauty. ✨",
"🌜 Sleep well! May your dreams be gentle and inspiring. 🌟",
"🌌 Good night! Rest well and let go of worries. 💫",
"💫 Sweet dreams! Sleep with a peaceful heart. 🌙",
"🌙 Sleep tight! May your night be filled with joy. 💖",
"💤 Good night! Rest and recharge for a beautiful tomorrow. 🌌",
"🌠 Sweet dreams! Let serenity fill your soul. ✨",
"🌜 Sleep well! May peace and calm surround you tonight. 🌟",
"🌌 Good night! Let your mind relax and drift happily. 💫",
"💫 Sweet dreams! Tomorrow is another day to shine. 🌙",
"🌙 Sleep tight! May your heart be happy and content. 💖",
"💤 Good night! Let the night bring comfort and rest. 🌌",
"🌠 Sweet dreams! May your sleep be restful and sweet. ✨",
"🌜 Sleep well! Drift peacefully into dreamland. 🌟",
"🌌 Good night! Let happiness guide your dreams tonight. 💫",
"💫 Sleep tight! May your night be magical and serene. 🌙",
"🌙 Sweet dreams! Let tomorrow bring you endless joy. 💖",
"💤 Good night! Rest your body, mind, and spirit. 🌌",
"🌠 Sleep well! Let stars fill your dreams with wonder. ✨",
"🌜 Good night! May your sleep be calm and relaxing. 🌟",
"🌌 Sweet dreams! Let peace and joy be with you. 💫",
"💫 Sleep tight! Tomorrow is full of possibilities. 🌙",
"🌙 Good night! Relax and enjoy the beauty of the night. 💖",
"💤 Sweet dreams! May your heart be happy and light. 🌌",
"🌠 Sleep well! Let the night inspire your dreams. ✨",
"🌜 Good night! Rest easy and wake up refreshed. 🌟",
"🌌 Sweet dreams! May your sleep be full of joy. 💫",
"💫 Sleep tight! Let the moonlight soothe your soul. 🌙",
"🌙 Good night! May your dreams be gentle and sweet. 💖",
"💤 Sweet dreams! Embrace the calmness of the night. 🌌",
"🌠 Sleep well! Let happiness fill your dreams tonight. ✨",
"🌜 Good night! Drift into sleep with peace and love. 🌟",
"🌌 Sweet dreams! May tomorrow bring you endless happiness. 💫",
"💫 Sleep tight! Rest well and dream beautifully. 🌙",
"🌙 Good night! Let the night wrap you in comfort and peace. 💖"
]


@Client.on_message(filters.command("gntag", ".") & filters.me)
async def gmtag(client: Client, message: Message):
    chat_id = message.chat.id
    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    # Pick a random quote for this spam
    quote = random.choice(RANDOM_QUOTES)
    async for usr in client.get_chat_members(chat_id):
        if chat_id not in spam_chats:
            break
        usrnum += 5
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 1:
            txt = f"<blockquote>{quote}</blockquote>\n<blockquote>✰| {usrtxt}</blockquote>"
            await client.send_message(chat_id, txt)
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
        return await message.edit("**It seems there is no gmtag here.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.edit("**Cancelled.**")


add_command_help(
    "gntag",
    [
        [
            "gntag",
            "Tag all the members with a random good night quote",
        ],
        [
            "cancel",
            "Stop the gntag spam",
        ],
    ],
)
