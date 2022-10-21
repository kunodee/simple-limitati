from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions.security import Security
from functions.database import Database
from functions.logs import logs
from decorators.admin import only_admins
from config import Config

@Client.on_callback_query(Config.cb_filter("start_command"), group=49)
async def _start_command(client, query):

    if(query.from_user.id in Config.in_chat): Config.in_chat.remove(query.from_user.id); logs.debug(f"{query.from_user.id} left the chat.")

    db = Database()
    db.add_user(query.from_user)
    db._close()

    if(await Security.is_admin(query.from_user.id)):
        btn = InlineKeyboardMarkup([[InlineKeyboardButton("🆘 Help", callback_data="help_command"), InlineKeyboardButton("👤 Users", callback_data="users_command")]])
        return await query.message.edit(Config.language['start']['admin'], reply_markup=btn)
    
    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Start Chat", callback_data="open_chat")]
    ])
    await query.message.edit(Config.language['start']['user'], reply_markup=btn)

@Client.on_message(filters.command("start") & filters.private, group=-100)
async def start_command(client, message):

    if(message.from_user.id in Config.in_chat): Config.in_chat.remove(message.from_user.id); logs.debug(f"{message.from_user.id} left the chat.")

    db = Database()
    db.add_user(message.from_user)
    logs.debug(f"{message.from_user.id} started the bot")
    db._close()

    if(await Security.is_admin(message.from_user.id)):
        btn = InlineKeyboardMarkup([[InlineKeyboardButton("🆘 Help", callback_data="help_command"), InlineKeyboardButton("👤 Users", callback_data="users_command")]])
        return await message.reply(Config.language['start']['admin'], reply_markup=btn)
    
    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Start Chat", callback_data="open_chat")]
    ])

    await message.reply(Config.language['start']['user'], reply_markup=btn)