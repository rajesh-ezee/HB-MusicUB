import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "8045459")) #optional
API_HASH = getenv("API_HASH", "e6d1f09120e17a4372fe022dde88511b") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1281282633 6773435708 7388810163").split()))
OWNER_ID = int(getenv("OWNER_ID", "1281282633"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://ghosttbatt:Ghost2021@ghosttbatt.ocbirts.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "7288055876:AAE5HtmRxqt_p03R4bfrXBp1IU7o4UkNesE")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://files.catbox.moe/r5hiwl.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "-1001735663878")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://t.me/GhosttBatt")
BRANCH = getenv("BRANCH", "main") #don't change

COMMAND_HANDLERS = []
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! > *").split())
#######################################
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')
#######################################
#Music_Assistant
STRING_SESSION = getenv("STRING_SESSION", "BQFwgJ0AZXUiuxNZCkWW_aiy2IUuX90I98C2PYlC96a1bT4RSrwsE8ZCMnlXL_y_tOsnn65s9IrwF1JApU8bwOFURzpWwqBf2nluztbJPM5i6XY51l5AmSvml0nEgbc1l7y9ULITR38CyJyAprewAwE18m0zE3gH1ACxTtj70JJ1JlDYb-zUtTTsJBAivu7xk7QGQ9AuLPCCcNTfGPEVrazpHXO-piRvVkE_Kzv797uI7xyL7mL1A0dFyuhSjkL8a8gnDA1r3hBsTJ00BLeSeSgc9T9shUDKoFxYuUym1AI55zRWIaGDW1HR5JMLDgdg6rQl3g84GO6Xq55M4cD5hqamgpBJZAAAAAErpzSyAA")
 
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
