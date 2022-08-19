from pyrogram import filters, Client 
from pyrogram.types import *
import os
from requests import get

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

pyrobot = Client("logomaker", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@pyrobot.on_message(filters.private, filters.incoming)
async def logomaker(_, message):
       if not message.text:
          await message.reply_text("send me text")
          return 
       elif message.text:
          text = message.text
          await message.reply_text("Processing your request")
          logo = get(f"https://single-developers.up.railway.app/logo?name={text}")
          await pyrobot.send_photo(message.chat.id, photo=logo)
       
      
      
      
pyrobot.run()
