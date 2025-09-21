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
    doc = {
        "_id": 1,
        "pmpermit": value,
        "pmpermit_message": PMPERMIT_MESSAGE,
        "block_message": BLOCKED,
        "limit": LIMIT,
    }
    r = await collection.find_one({"_id": 1})
    if r:
        await collection.update_one({"_id": 1}, {"$set": {"pmpermit": value}})
    else:
        # 🚀 Insert defaults if not exists
        await collection.insert_one(doc)

    # Ensure Approved list exists
    if not await collection.find_one({"_id": "Approved"}):
        await collection.insert_one({"_id": "Approved", "users": []})


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
        return True, PMPERMIT_MESSAGE, LIMIT, BLOCKED  # 🚀 Safe defaults

    pmpermit = result.get("pmpermit", True) #PmGurd on - True
    pm_message = result.get("pmpermit_message") or PMPERMIT_MESSAGE
    block_message = result.get("block_message") or BLOCKED
    limit = result.get("limit", LIMIT)

    return pmpermit, pm_message, limit, block_message
