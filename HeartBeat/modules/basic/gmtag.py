from asyncio import sleep
import random

from pyrogram import Client, filters
from pyrogram.types import Message

from HeartBeat.modules.help import add_command_help

spam_chats = []

# Some random quotes pool
RANDOM_QUOTES = [
"🌞 Good morning! Rise and shine to a beautiful day ahead! 🌸",
"☕ Wake up, smile, and enjoy the magic of today! 🌼",
"🌅 Every sunrise brings new hope and endless possibilities! ✨",
"💛 Good morning! Fill your day with love, joy, and laughter! 😄",
"🌻 Wake up and be awesome! The world is waiting for you! 🌟",
"☀️ Today is a fresh start! Make it count! 🌈",
"🌺 Good morning! Let your heart be light and your mind be calm! 🍃",
"🌞 Rise up and embrace all the beauty around you! 💖",
"☕ Start your day with gratitude and positivity! 🌷",
"🌅 Good morning! Today is a perfect day to chase your dreams! 💫",
"💛 Smile! A beautiful day awaits you! 🌻",
"🌻 Wake up with energy and let happiness flow through you! 🌸",
"☀️ Every morning is a new opportunity to shine! ✨",
"🌺 Good morning! Let your soul bloom like flowers! 🌼",
"🌞 Rise and shine! Let today be full of joy and laughter! 😍",
"☕ A cup of positivity and a sprinkle of happiness to start your day! 🌈",
"🌅 Good morning! The world looks brighter with your smile! 💖",
"💛 Wake up and make today unforgettable! 🌟",
"🌻 Smile! A new day brings endless opportunities! 🌸",
"☀️ Good morning! Let your dreams guide you today! 💫",
"🌺 Wake up with courage, hope, and positivity! 🌼",
"🌞 Good morning! Let your heart be full of happiness! 💖",
"☕ Start your day with love and gratitude! 🌷",
"🌅 Rise and shine! Make today amazing! ✨",
"💛 Good morning! Embrace the little joys of life! 🌻",
"🌻 Wake up with a smile and a grateful heart! 🌸",
"☀️ Good morning! Today is another chance to shine! 🌟",
"🌺 Let your positivity brighten everyone’s day! 💫",
"🌞 Good morning! Happiness begins with you! 🌼",
"☕ A beautiful day begins with a beautiful mindset! 🌷",
"🌅 Good morning! Chase your dreams with confidence! ✨",
"💛 Wake up and let your light shine bright! 🌻",
"🌻 Good morning! Spread kindness everywhere you go! 🌸",
"☀️ Start today with courage and determination! 💖",
"🌺 Good morning! Make your heart happy today! 🌼",
"🌞 Smile and let your energy inspire others! 🌟",
"☕ Good morning! Each day is a gift—unwrap it with joy! 🌈",
"🌅 Wake up and embrace all the wonderful moments today! 💫",
"💛 Good morning! Life is beautiful, enjoy every bit! 🌻",
"🌻 Rise and shine! Let positivity guide you! 🌸",
"☀️ Good morning! Believe in yourself and achieve greatness! 🌟",
"🌺 Wake up with hope and endless dreams! 💖",
"🌞 Good morning! Start your day with a happy heart! 🌼",
"☕ Today is full of magic, grab it with a smile! 🌷",
"🌅 Good morning! Every step you take leads to success! ✨",
"💛 Wake up and make today count! 🌻",
"🌻 Good morning! Let love and peace fill your day! 🌸",
"☀️ Rise and shine! Opportunities await you! 💫",
"🌺 Good morning! Make today a masterpiece! 🌼",
"🌞 Smile! The universe is full of wonders for you! 🌟",
"☕ Start the day with a grateful heart! 💖",
"🌅 Good morning! Spread happiness wherever you go! 🌷",
"💛 Wake up and embrace the beauty of life! 🌻",
"🌻 Good morning! Be positive and shine bright! 🌸",
"☀️ Rise with energy and enthusiasm! ✨",
"🌺 Good morning! Let every moment be joyful! 💫",
"🌞 Smile and enjoy the blessings of today! 🌼",
"☕ Wake up to a world full of love and possibilities! 💖",
"🌅 Good morning! Take a deep breath and relax! 🌷",
"💛 Start today with hope and excitement! 🌻",
"🌻 Good morning! Shine your light and inspire others! 🌸",
"☀️ Wake up and be the best version of yourself! 🌟",
"🌺 Good morning! Let positivity guide your path! 💫",
"🌞 Rise and shine! Life is a beautiful journey! 🌼",
"☕ Good morning! Keep smiling and stay blessed! 🌷",
"🌅 Start your day with joy and happiness! ✨",
"💛 Good morning! Your smile can change the world! 🌻",
"🌻 Wake up with determination and confidence! 🌸",
"☀️ Good morning! Let gratitude fill your heart! 💖",
"🌺 Smile and enjoy every little thing today! 🌼",
"🌞 Good morning! Today is a gift, cherish it! 🌟",
"☕ Wake up with energy and positivity! 🌷",
"🌅 Good morning! Let your soul shine bright! ✨",
"💛 Start your day with love and kindness! 🌻",
"🌻 Good morning! Chase dreams and make them real! 🌸",
"☀️ Rise and shine! Let happiness lead the way! 💫",
"🌺 Good morning! Each day is full of possibilities! 🌼",
"🌞 Wake up and embrace the beauty around you! 🌟",
"☕ Good morning! Smile and make today amazing! 🌷",
"🌅 Start today with courage and hope! ✨",
"💛 Good morning! Be happy and spread joy! 🌻",
"🌻 Wake up and shine with positivity! 🌸",
"☀️ Good morning! Let your heart guide your day! 💖",
"🌺 Smile! Today is full of opportunities! 🌼",
"🌞 Good morning! Make your dreams come true! 🌟",
"☕ Rise and shine! Life is beautiful and full of love! 🌷",
"🌅 Good morning! Keep smiling, keep shining! ✨",
"💛 Wake up and embrace every blessing today! 🌻",
"🌻 Good morning! Fill your heart with happiness! 🌸",
"☀️ Start your day with a grateful mindset! 💫",
"🌺 Good morning! Let love and positivity flow! 🌼",
"🌞 Smile and let today be your masterpiece! 🌟",
"☕ Good morning! Life is better with a smile! 🌷",
"🌅 Wake up and spread kindness everywhere! ✨",
"💛 Good morning! Embrace the beauty of a new day! 🌻",
"🌻 Rise with joy and confidence! 🌸",
"☀️ Good morning! Keep shining bright and stay happy! 💖",
"🌺 Start today with hope, love, and positivity! 🌼",
"🌞 Good morning! The best is yet to come! 🌟",
"☕ Wake up and make each moment count! 🌷",
"🌅 Good morning! Let happiness be your guide today! ✨",
"💛 Smile and embrace the wonders of life! 🌻",
"🌻 Good morning! Fill your day with love and laughter! 🌸",
"☀️ Rise and shine! A new adventure awaits you! 💫",
"🌺 Good morning! Start today with a heart full of gratitude! 🌼",
"🌞 Smile! Today is a perfect day for new beginnings! 🌟",
"☕ Good morning! Live, love, and laugh today! 🌷",
"🌅 Wake up and be thankful for this beautiful life! ✨"
]

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


@Client.on_message(filters.command("gmtag", ".") & filters.me)
async def mentionall(client: Client, message: Message):
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)

    # If no reply and no text → tagging will use random quotes per user
    use_random_quotes = False
    if not direp and not args:
        use_random_quotes = True

    await message.delete()
    spam_chats.append(chat_id)

    async for usr in client.get_chat_members(chat_id):
        if chat_id not in spam_chats:
            break

        mention = f"[{usr.user.first_name}](tg://user?id={usr.user.id})"

        if use_random_quotes:
            text = f"<blockquote>{random.choice(RANDOM_QUOTES)}</blockquote>\n<blockquote>✰| {mention}</blockquote>"
            await client.send_message(chat_id, text)
        elif args:
            text = f"<blockquote>{args}</blockquote>\n<blockquote>✰| {mention}</blockquote>"
            await client.send_message(chat_id, text)
        elif direp:
            await direp.reply(mention)

        await sleep(2)

    try:
        spam_chats.remove(chat_id)
    except:
        pass


@Client.on_message(filters.command("cancel", ".") & filters.me)
async def cancel_spam(client: Client, message: Message):
    if message.chat.id not in spam_chats:
        return await message.edit("**It seems there is no goodmorning tag here.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.edit("**Cancelled.**")


add_command_help(
    "gmtag",
    [
        [
            "gmtag",
            "Tag all the members one by one. If each user will get a random quote.",
        ],
        [
            "cancel",
            "to stop .tagall",
        ],
    ],
)
