from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions.security import Security
from functions.logs import logs
from functions.database import Database
from datetime import datetime
from config import Config

@Client.on_message(filters.private, group=60)
async def in_chat(client, message):

    if await Security.is_admin(message.from_user.id):
        reply_to = message.reply_to_message
        if(str(message.text).startswith("/")): return
        if(not reply_to): return
        if(not reply_to.entities): return
        if(not len(reply_to.entities) >= 2): return
        if(not reply_to.entities[1].user): return
        
        user = reply_to.entities[1].user
        await message.forward(user.id, message)

    if message.from_user.id in Config.in_chat:

        if(not await Security.is_admin(message.from_user.id)):
            for admin in Config.admins:
                await client.send_message(admin, f"• **Message from** {message.from_user.mention} __({message.from_user.id})__\n\n🔁 **REPLY TO THIS MESSAGE FOR ANSWER**")
                await message.forward(admin, message)
            return