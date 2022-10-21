from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions.security import Security
from functions.database import Database
from functions.logs import logs
from datetime import datetime
from config import Config

@Client.on_callback_query(Config.cb_filter("users_command"), group=48)
async def users_command(client, query):

    db = Database()
    rows = db.get_users()
    db._close()

    message = """👤 **Users List**:\n\n"""

    for user in rows:
        message += f"• ({user[0]}) __{user[1]}__ - {datetime.fromtimestamp(user[2])}\n"

    message += f"""\n» **Total ({len(rows)}) user/s**"""

    await query.message.edit(message, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="start_command")]]))