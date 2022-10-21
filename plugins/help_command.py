from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions.security import Security
from config import Config

@Client.on_callback_query(Config.cb_filter("help_command"), group=50)
async def help_command(client, query):
    await query.message.edit(Config.language['help'], reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="start_command")]]))