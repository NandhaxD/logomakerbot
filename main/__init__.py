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

support = "nandhasupport"
updates = "nandhabots"
#logo api's
LOGO_API_URL0 = "https://api.sdbots.tk/anime-logo?name="
LOGO_API_URL1 = "https://techzbotsapi.herokuapp.com/logo?text="
LOGO_API_URL2 = "https://techzbotsapi.herokuapp.com/logo?square=true&text="

#Cilent start
pyrobot = Client("nandhabot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="{}/plugins".format(__name__)))

