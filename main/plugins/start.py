from pyrogram import filters
from pyrogram.types import *
from main import pyrobot, support, updates

START_text = """**Hello,** {}
**Iam A LogomakingBot I can make logo for you 

use: /logo name | for normal logos. 
use: /slogo name | for square type logos.**
"""

Buttons = [[ InlineKeyboardButton(text="Support", url=f"t.me/{support}"),
             InlineKeyboardButton(text="Updates", url=f"t.me/{updates}")]]
  
  
@pyrobot.on_message(filters.command("start"))
async def start(_, message):
      await message.reply_photo(photo="https://telegra.ph/file/f1958a5500458504879a7.jpg",
      START_text.format(message.from_user.mention),reply_markup=InlineKeyboardMarkup(Buttons))
