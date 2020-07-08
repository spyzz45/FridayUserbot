"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
ALIVE_IMG = "https://telegra.ph/file/1a4c1987b71cdb9c01bbe.mp4"
ALIVE_caption = "`📷FRIDAY IS📷:` **ONLINE**\n\n"
ALIVE_caption += "**🤖SYSTEM STATUS🤖**\n\n"
ALIVE_caption += "`🔰TELETHON VERSION🔰:` **6.0.9**\n`Python:` **3.7.4**\n\n"
ALIVE_caption += "`👉🏻DATABASE STATUS👈🏻:` **Functional**\n\n"
ALIVE_caption += "**👹Current Branch👹** : `master`\n\n"
ALIVE_caption += "**🍁Friday OS🍁** : `3.14`\n\n"
ALIVE_caption += "**🚵Current Sat🚵** : `@whitedevil-2.25`\n\n"
ALIVE_caption += f"**🍁My right full owner🍁** : {DEFAULTUSER} \n\n"
ALIVE_caption += "**🌿Heroku Database🌿** : `AWS - Working Properly`\n\n"
ALIVE_caption += "**✌️License✌️** : [MIT Licence](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n\n"
ALIVE_caption += "Copyright By [@Github](GitHub.com)\n\n"
ALIVE_caption += "[Deploy FridayUserbot](https://telegra.ph/FRIDAY-06-15)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, ALIVE_IMG,caption=ALIVE_caption)
