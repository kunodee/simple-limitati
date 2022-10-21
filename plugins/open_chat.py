from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions.security import Security
from functions.logs import logs
from functions.database import Database
from datetime import datetime
from config import Config

@Client.on_callback_query(Config.cb_filter("open_chat"), group=47)
async def open_chat(client, query):

    db = Database()
    if(db.is_banned(query.from_user)):
        await query.message.edit(Config.language['banned'], reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="start_command")]]))
        logs.debug(f"{query.from_user.id} is banned from the chat")
        db._close()
        return
    
    if(query.from_user.id in Config.in_chat):
        await query.message.edit(Config.language['already_in_chat'], reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="start_command")]]))
        logs.debug(f"{query.from_user.id} is already in chat")
    else:
        logs.debug(f"{query.from_user.id} is now in chat")
        await query.message.edit(Config.language['chat_now'], reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="start_command")]]))
        Config.in_chat.append(query.from_user.id)
