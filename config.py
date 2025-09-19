import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "8045459")) #optional
API_HASH = getenv("API_HASH", "e6d1f09120e17a4372fe022dde88511b") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1281282633").split()))
OWNER_ID = int(getenv("OWNER_ID", "1281282633"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://ghosttbatt:Ghost2021@ghosttbatt.ocbirts.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "8244250546:AAFn8oG3iZWaPrvEP0tTRH5K0-eBQgqY3y8")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/9ee37cccd7bf55c3ec953.png')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "-1001735663878")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://t.me/GhosttBatt")
BRANCH = getenv("BRANCH", "main") #don't change

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! > *").split())
    #######################################
    for x in COMMAND_PREFIXES:
        COMMAND_HANDLERS.append(x)
    COMMAND_HANDLERS.append('')
    #######################################
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
