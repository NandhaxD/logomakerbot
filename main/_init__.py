from pyrogram import filters, Client 
from pyrogram.types import *
import os
from requests import get
import aiohttp

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

print("[INFO]: STARTING AIOHTTP CLIENT")
session = aiohttp.ClientSession()

#logo api's
LOGO_API_URL1 = "https://techzbotsapi.herokuapp.com/logo?text="
LOGO_API_URL2 = "https://techzbotsapi.herokuapp.com/logo?square=true&text="

#Cilent start
pyrobot = Client("logomaker", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)   
      
print("[INFO]: STARTING BOT...")
app.start()
