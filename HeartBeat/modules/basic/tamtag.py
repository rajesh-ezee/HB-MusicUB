from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message
import random

from HeartBeat.modules.help import add_command_help

spam_chats = []

# Pool of good morning quotes
RANDOM_QUOTES = [
"Hey epdi 😎 irukka?",
"Coffe kudichitaya ☕ illaya?",
"Inaiku Collage 🏫 ila na office ponaya 💼?",
"Eppo VC-ku 📱 varuva?",
"Yenakku call pannitu 🤔 pesura?",
"Snack ready 🍪 panita?",
"Wifi slow aa 🌐 irukku illa fast aa?",
"Friend kitta jokes share 😂 pannita?",
"Thanni kudichita 💧?",
"Movie plan 🎬 pannira?",
"Morning walk 🚶‍♂️ pogira?",
"Exam pass aayiducha 📝?",
"Sleep full aayita 🛌?",
"Online class 💻 attend pannita?",
"Pizza order 🍕 pannita?",
"Gym ku poita 💪?",
"Crush message 💌 anupita?",
"Traffic la stuck aa 🚦?",
"Tea ready aa 🍵?",
"Dog walk 🐕 pannita?",
"Bus catch pannita 🚌?",
"Game play 🎮 pannita?",
"Shopping pannita 🛒?",
"Weekend plan set aayita 📅?",
"Story update 📸 pannita?",
"Sleep early pannita 🌙?",
"Breakfast ready aa 🥐?",
"Car wash pannita 🚗?",
"New meme paakitta 😂?",
"Friend party ku poita 🥳?",
"Bike ride 🏍️ pannita?",
"Work start pannita 💻?",
"Movie paakara 🍿?",
"Music listen 🎧 pannita?",
"Coffee strong aa irukku ☕?",
"Morning yoga 🧘‍♂️ pannita?",
"Class la nap 😴 pannita?",
"Online shopping 🛍️ pannita?",
"Food ready aa 🍲?",
"Meeting start aayita 🏢?",
"Dog feed 🐶 pannita?",
"TV series paaka 📺 start pannita?",
"Snack ready aa 🍪?",
"Friend call 📞 pannita?",
"Car petrol fill pannita ⛽?",
"Weekend la relax 🛋️ pannita?",
"Morning alarm silent aa ⏰ irukku?",
"Gym membership renew pannita 💪?",
"Birthday wish send pannita 🎂?",
"Tea strong aa kudichita 🍵?",
"Study start pannita 📚?",
"VC ku ready aa 📱 irukka?",
"Evening walk pogira 🌇?",
"New song listen pannita 🎶?",
"Breakfast eat pannita 🍳?",
"Friend house ku poi irukka 🏡?",
"Coffee refill pannita ☕?",
"Dog bath pannita 🐕💦?",
"Movie theatre ku poi irukka 🎬?",
"Game update pannita 🎮?",
"Traffic jam la stuck aa 🚗?",
"Snack order pannita 🍕?",
"Meeting end aayita 🏢?",
"Friend kitta joke share 😂 pannita?",
"New dress try pannita 👗?",
"Tea time aa 🍵?",
"Sleep time ready aa 🛌?",
"Online exam attend pannita 💻?",
"Car start pannita 🚗?",
"Dog play pannita 🐶?",
"Coffee strong aa kudichita ☕?",
"Movie paaka ready aa 🍿?",
"Friend kitta message send pannita 📱?",
"Gym session start pannita 💪?",
"Study material ready aa 📚?",
"Pizza delivery vachita 🍕?",
"Weekend trip plan pannita 🚗🗺️?",
"VC la silent aa irukka 📱?",
"Evening tea kudichita 🍵?",
"Dog feed pannita 🐕?",
"Morning alarm set pannita ⏰?",
"Friend house ku poi irukka 🏡?",
"Music playlist ready aa 🎶?",
"Coffee cup refill pannita ☕?",
"Snack taste pannita 🍪?",
"Movie paaka seat book pannita 🎬?",
"Online class mute pannita 💻?",
"Car wash pannita 🚗?",
"Game level complete pannita 🎮?",
"Friend kitta video share pannita 📹?",
"Dog walk pannita 🐕?",
"Evening walk start pannita 🌇?",
"Birthday gift ready aa 🎁?",
"Breakfast eat pannita 🍳?",
"Sleep full aa 🛌?",
"Morning exercise pannita 🏃‍♂️?",
"Coffee cup ready aa ☕?",
"Snack taste pannita 🍕?",
"TV series watch pannita 📺?",
"Friend message read pannita 📱?",
"Weekend la chill pannita 🛋️?",
"Dog play pannita 🐶?",
"New song listen pannita 🎶?",
"Movie paaka ready aa 🍿?",
"Online game start pannita 🎮?",
"Gym ku ready aa 💪?",
"Tea strong aa kudichita 🍵?",
"Friend call pannita 📞?",
"Study start pannita 📚?",
"VC ku poi irukka 📱?"
]

@Client.on_message(filters.command("tamtag", ".") & filters.me)
async def gmtag(client: Client, message: Message):
    chat_id = message.chat.id
    await message.delete()
    spam_chats.append(chat_id)
    
    async for member in client.get_chat_members(chat_id):
        if chat_id not in spam_chats:
            break
        
        user = member.user
        if user.is_bot:  # skip bots
            continue
        
        quote = random.choice(RANDOM_QUOTES)  # random quote per user
        txt = f"<blockquote>{quote}</blockquote>\n<blockquote>✰| [{user.first_name}](tg://user?id={user.id})</blockquote>"
        
        await client.send_message(chat_id, txt)
        await sleep(2)  # avoid flood
    
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@Client.on_message(filters.command("cancel", ".") & filters.me)
async def cancel_spam(client: Client, message: Message):
    if message.chat.id not in spam_chats:
        return await message.edit("**It seems there is no tamtag here.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.edit("**Cancelled.**")


add_command_help(
    "tamtag",
    [
        [
            "tamtag",
            "Tag all the members with a random tamil quote",
        ],
        [
            "cancel",
            "Stop the tamtag spam",
        ],
    ],
)
