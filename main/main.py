from pyrogram import filters, Client 
from pyrogram.types import *
import os
from requests import get

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

pyrobot = Client("logomaker", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

from main import LOGO_API_URL1, LOGO_API_URL2, session
from typing import Optional
import aiohttp

async def generate_logo(text: str, square: Optional[bool] = False ):
  "To Create Logos. text = What you want to write on the logo. square = If You Want Square Logo Or Not. Returns Telgraph Image Url"
  
  try:
    square = str(square).capitalize()
  
    if square == "True":
      url = LOGO_API_URL2 + text
    else:
      url = LOGO_API_URL1 + text
  
    resp = await session.get(url)  
    img_url = resp.url
  except Exception as e:
    return "error" + str(e)
      
  return str(img_url)
      
      
      
pyrobot.run()
