from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions.security import Security
from functions.logs import logs
from decorators.admin import only_admins
from functions.database import Database
from datetime import datetime
from config import Config

@Client.on_message(filters.command("bans"), group=-98)
@only_admins
async def bans_command(client, message):
    db = Database()
    rows = db.get_bans()
    db._close()

    _message = """👤 **Bans List**:\n\n"""

    for user in rows:
        _message += f"• ({user[0]}) __{user[1]}__\n"

    _message += f"""\n» **Total ({len(rows)}) user/s**"""
    logs.debug(f"{message.from_user.id} used /bans command.")

    await message.reply(_message)
