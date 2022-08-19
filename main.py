from pyrogram import filters, Client 
from pyrogram.types import *
import os
from requests import get

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

pyrobot = Client("logomaker", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.private, filters.incoming)
async def logomaker(_, message):
       if message.text:
          await message.reply_text("send me text")
          return 
       elif message.text:
          text = message.text
          logo = get((f"https://single-developers.up.railway.app/logo?name={text}").replace(' ','%20')).history[1].url
          await bot.send_photo(message.chat.id, photo=logo)
       
      
      
      
pyrobot.run()
