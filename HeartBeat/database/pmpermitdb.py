from HeartBeat.database import cli
import asyncio

collection = cli["HeartBeat"]["pmpermit"]

# Default PM Permit message
PMPERMIT_MESSAGE = """**<blockquote>☆ . * ● ¸ . ✦ .★° :. ★ * • ○ ° ★</blockquote>
<blockquote>ʜᴇʏ, ɪ'ᴍ 𝐇𝐞𝐚𝐫𝐭𝐁𝐞𝐚𝐭-✗-𝐁𝐨𝐭</blockquote>
<blockquote>➽───────────────❥</blockquote>
<blockquote>💕 ᴛᴀɢ ᴍʏ ʟᴏᴠᴇ 🦋  
🔗 https://t.me/HeartBeat_Fam</blockquote>
<blockquote>➽───────────────❥</blockquote>
<blockquote>😈 ᴏᴛʜᴇʀᴡɪꜱᴇ, ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴍʏ ʙᴏꜱꜱ ᴄᴏᴍᴇꜱ.  
🚫 ᴅᴏɴ'ᴛ ꜱᴘᴀᴍ ᴍᴇ – ʏᴏᴜ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ʙʟᴏᴄᴋᴇᴅ (ᴜᴘ ᴛᴏ 3 ᴡᴀʀɴɪɴɢꜱ).</blockquote>
<blockquote>☆ . * ● ¸ . ✦ .★° :. ★ * • ○ ° ★</blockquote>"""

# Default block message
BLOCKED = "**<blockquote>ʙᴇᴇᴘ ʙᴏᴏᴘ ꜰᴏᴜɴᴅᴇᴅ ᴀ ꜱᴘᴀᴍᴍᴇʀ!, ʙʟᴏᴄᴋᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!</blockquote>**"

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
