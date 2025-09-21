from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message
import random

from HeartBeat.modules.help import add_command_help

spam_chats = []

# Pool of good morning quotes

RANDOM_QUOTES = [
"Hey 😎 VC-ku vara ready-aa?",
"Eppo 📱 join pannura VC-ku?",
"Coffe 🍵 kudichitu VC-la join pannala?",
"Inaiku 🏫 college illa, VC-ku irukkomla?",
"Friend 👬 ellam VC-ku vara irukka?",
"Morning walk 🚶‍♂️ mudincha, VC-la join pannu!",
"Movie 🎬 paatha, VC-ku povomla?",
"Game 🎮 start pannitu VC-ku vara?",
"Snack 🍕 ready pannita, VC-la join pannala?",
"Coffee ☕ kudicha, VC-ku ready-aa?",
"Evening walk 🌇 aachu, VC-la irukkala?",
"Dog 🐕 walk panna mudichitu VC-ku join pannala?",
"New song 🎶 paatha, VC-la irukka?",
"Friend kitta joke 😂 share pannitu VC-ku vara?",
"Traffic 🚦 jam-la irundha, VC-la join panna ready-aa?",
"Breakfast 🥐 mudincha, VC-ku join pannala?",
"TV 📺 paathitu VC-ku vara irukka?",
"Online class 💻 mudichitu VC-ku join pannala?",
"Pizza 🍕 order pannitu VC-la vara ready-aa?",
"Gym 💪 finish pannitu VC-ku vara?",
"VC-ku 📱 ellam ready-aa irukka?",
"Study 📚 mudichitu VC-ku join pannala?",
"Sleep 🛌 short aayita, VC-ku vara?",
"Evening tea 🍵 kudicha, VC-ku join pannala?",
"Weekend plan 📅 set pannitu VC-la vara ready-aa?",
"Friend house 🏡 visit pannitu VC-ku join pannala?",
"Movie theatre 🎬 mudichitu VC-ku vara ready-aa?",
"Game update 🎮 pannitu VC-la join pannala?",
"Traffic jam 🚗 mudichitu VC-ku vara?",
"Snack 🍪 ready aa, VC-ku join pannala?",
"Car wash 🚗 finish pannitu VC-ku join pannala?",
"Music playlist 🎧 ready-aa, VC-ku vara?",
"Birthday gift 🎁 ready pannitu VC-ku join pannala?",
"Morning alarm ⏰ set pannitu VC-ku join pannala?",
"Coffee cup ☕ refill pannitu VC-ku vara ready-aa?",
"Dog 🐕 bath pannitu VC-la join pannala?",
"TV series 📺 watch pannitu VC-ku vara?",
"Friend message 📱 read pannitu VC-ku join pannala?",
"Evening walk 🌇 mudichitu VC-ku vara?",
"Gym session 💪 finish pannitu VC-ku join pannala?",
"Snack taste 🍕 pannitu VC-ku vara ready-aa?",
"Online game 🎮 start pannitu VC-ku join pannala?",
"Movie 🍿 paaka ready aa, VC-ku join pannala?",
"Coffee ☕ strong aa kudichitu VC-ku vara?",
"Friend call 📞 pannitu VC-ku join pannala?",
"Study 📚 finish pannitu VC-la vara ready-aa?",
"VC-ku 📱 ellam ready aa irukka?",
"Dog 🐕 play pannitu VC-ku join pannala?",
"Pizza 🍕 delivery vachitu VC-la vara ready-aa?",
"Evening tea 🍵 kudichitu VC-ku join pannala?",
"Class 💻 mudichitu VC-ku vara ready-aa?",
"Car start 🚗 pannitu VC-ku join pannala?",
"Music 🎶 playlist ready aa, VC-ku vara?",
"Snack 🍪 ready pannitu VC-la join pannala?",
"Friend kitta joke 😂 share pannitu VC-ku vara?",
"Movie 🎬 paaka seat book pannitu VC-la join pannala?",
"Online class 💻 mute pannitu VC-ku vara ready-aa?",
"Car wash 🚗 finish pannitu VC-la join pannala?",
"Game level complete 🎮 pannitu VC-ku vara?",
"Friend kitta video share 📹 pannitu VC-la join pannala?",
"Dog 🐕 walk pannitu VC-ku join pannala?",
"Evening walk start 🌇 pannitu VC-ku vara?",
"Birthday gift 🎁 ready pannitu VC-la join pannala?",
"Breakfast 🥐 eat pannitu VC-ku vara?",
"Sleep 🛌 full aa, VC-la join pannala?",
"Morning exercise 🏃‍♂️ pannitu VC-ku vara?",
"Coffee cup ☕ ready aa, VC-ku join pannala?",
"Snack 🍕 taste pannitu VC-la vara?",
"TV series 📺 watch pannitu VC-ku join pannala?",
"Friend message 📱 read pannitu VC-ku vara?",
"Weekend la chill 🛋️ pannitu VC-ku join pannala?",
"Dog 🐶 play pannitu VC-la vara?",
"New song 🎶 listen pannitu VC-ku join pannala?",
"Movie paaka 🍿 ready aa, VC-la join pannala?",
"Online game 🎮 start pannitu VC-ku vara?",
"Gym 💪 ku ready aa, VC-la join pannala?",
"Tea strong aa kudicha 🍵, VC-ku join pannala?",
"Friend call 📞 pannitu VC-la vara?",
"Study start pannita 📚, VC-ku vara ready-aa?",
"VC-ku 📱 ellam ready-aa irukka?",
"Evening tea 🍵 kudicha, VC-ku join pannala?",
"Dog 🐕 feed pannitu VC-ku vara?",
"Morning alarm set pannita ⏰, VC-ku join pannala?",
"Friend house 🏡 ku poi irukka, VC-la vara ready-aa?",
"Music playlist 🎶 ready aa, VC-ku join pannala?",
"Coffee cup refill pannitu ☕, VC-la vara?",
"Snack taste pannitu 🍪, VC-ku join pannala?",
"Movie paaka seat book pannitu 🎬, VC-ku vara?",
"Online class mute pannitu 💻, VC-la join pannala?",
"Car wash pannitu 🚗, VC-ku join pannala?",
"Game level complete pannitu 🎮, VC-la vara ready-aa?",
"Friend kitta video share pannitu 📹, VC-ku join pannala?",
"Dog walk pannitu 🐕, VC-la vara ready-aa?",
"Evening walk start pannitu 🌇, VC-ku join pannala?",
"Birthday gift 🎁 ready pannitu, VC-la join pannala?",
"Breakfast eat pannitu 🥐, VC-ku vara ready-aa?"
]

@Client.on_message(filters.command("vctag", ".") & filters.me)
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
        return await message.edit("**It seems there is no vctag here.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.edit("**Cancelled.**")


add_command_help(
    "vctag",
    [
        [
            "vctag",
            "Tag all the members with a random good morning quote",
        ],
        [
            "cancel",
            "Stop the vctag spam",
        ],
    ],
)
