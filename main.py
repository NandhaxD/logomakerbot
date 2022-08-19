from telethon import TelegramClient
import logging
import os
import config 
import random
import glob
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterPhotos
from telethon import events, Button, custom
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
import requests


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)




tbot = TelegramClient("logomakerbot", API_ID, API_HASH)



def register(**args):
    """ Registers a new message. """
    pattern = args.get('pattern', None)

    r_pattern = r'^[/!]'

    if pattern is not None and not pattern.startswith('(?i)'):
        args['pattern'] = '(?i)' + pattern

    args['pattern'] = pattern.replace('^/', r_pattern, 1)

    def decorator(func):
        telethn.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator

@register(pattern="^/logo ?(.*)")
async def logo_gen(event):
    xx = await event.reply("**ᴘʀᴇᴘᴀʀɪɴɢ ʟᴏɢᴏ**")
    name = event.pattern_match.group(1)
    if not name:
        await xx.edit("`Provide some text to draw!\nExample: /logo <your name>!`")
        return
    bg_, font_ = "", ""
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            if hasattr(temp.media, "document"):
                if "font" in temp.file.mime_type:
                    font_ = await temp.download_media()
                elif (".ttf" in temp.file.name) or (".otf" in temp.file.name):
                    font_ = await temp.download_media()
            elif "pic" in mediainfo(temp.media):
                bg_ = await temp.download_media()
    else:
        pics = []
        async for i in ubot2.iter_messages(
            "@WolfXLogopack", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download_media()
        fpath_ = glob.glob("./WolfXRobot/resources/fonts/*")
        font_ = random.choice(fpath_)
    if not bg_:
        pics = []
        async for i in ubot2.iter_messages(
            "@WolfXLogopack", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download_media()
    if not font_:
        fpath_ = glob.glob("./WolfXRobot/resources/fonts/*")
        font_ = random.choice(fpath_)
    if len(name) <= 8:
        fnt_size = 120
        strke = 10
    elif len(name) >= 9:
        fnt_size = 50
        strke = 5
    else:
        fnt_size = 100
        strke = 20
    img = Image.open(bg_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_, fnt_size)
    w, h = draw.textsize(name, font=font)
    h += int(h * 0.21)
    image_width, image_height = img.size
    draw.text(
        ((image_width - w) / 2, (image_height - h) / 2),
        name,
        font=font,
        fill=(255, 255, 255),
    )
    x = (image_width - w) / 2
    y = (image_height - h) / 2
    draw.text((x, y), name, font=font, fill="white",
              stroke_width=strke, stroke_fill="black")
    flnme = f"logo.png"
    img.save(flnme, "png")
    ii = await xx.edit("📩 **ᴜᴘʟᴏᴀᴅɪɴɢ**")
    if os.path.exists(flnme):
        await tbot.send_file(
            event.chat_id,
            file=flnme,
            caption="━━━━━━━  Wᴏʟғ  X  ━━━━━━━\n\n☘️ ᴛʜɪꜱ ɪꜱ ʏᴏᴜʀ ᴘʀᴏꜰɪʟᴇ ᴘɪᴄᴛᴜʀᴇ ☘️\n◈──────────────◈\n🔥 ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ : [Wᴏʟғ  X  Rᴏʙᴏᴛ](https://t.me/Cringe_Botz)\n⚡️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [Cʀɪɴɢe  Gᴜʏs](https://t.me/Tamilchat_cringe_Guys)\n◈──────────────◈\n©2021 [Cʀɪɴɢe X Nᴇᴛᴡᴏʀᴋ](https://t.me/Cringe_X_NetWork)™ ᴛᴇᴀᴍ\nʀᴇꜱᴇʀᴠᴇᴅ ᴀʟʟ ʀɪɢʜᴛ ⚠️️\n\n━━━━━━━  Wᴏʟғ  X  ━━━━━━━", buttons=BUTTON,
            force_document=False,
        )
        os.remove(flnme)
        await ii.delete()
    if os.path.exists(bg_):
        os.remove(bg_) 
    if os.path.exists(font_):
        if not font_.startswith("./WolfXRobot/resources/fonts"):
            os.remove(font_)
