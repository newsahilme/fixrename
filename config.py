# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "17540447")

API_HASH = os.environ.get("API_HASH", "8ffa3ede58cd9957f178765dd969ab3e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6477035546:AAHJJWkVQv86ZeOrrO_c5C79DP4cBehF7cc") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Anime_X_Hunters") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "netflixvro59")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://netflixvro59:Anonymous_me6@cluster0.ykgvswy.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/294de152b96b93cdb3daf.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5090651635').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
