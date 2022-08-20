from main import pyrobot, support 
from pyrogram import __version__ as pyrover

if __name__ == "__main__":
   pyrobot.run()
   with pyrobot:
      pyrobot.send_message(f"@{support}",f"**Iam online Now!**\n**Pyroverion: {pyrover}**")
