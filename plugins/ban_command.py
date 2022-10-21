from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions.security import Security
from functions.logs import logs
from decorators.admin import only_admins
from functions.database import Database
from datetime import datetime
from config import Config

@Client.on_message(filters.command("ban"), group=-99)
@only_admins
async def ban_command(client, message):
    userID = None
    _a = 0
    if(len(message.command) >= 2):
        userID = " ".join(message.command[1:]).split(" ")[0]

    db = Database()

    if userID:
        try: userID = int(userID)
        except: await message.reply(Config.language['invalid_userid']); return db._close()

        if userID == message.from_user.id: 
            await message.reply(Config.language['cannot_ban_urself']); return db._close()

        if await Security.is_admin(userID):
            await message.reply(Config.language['cannot_ban_an_admin']); return db._close()

        user = db.get_user(userID)

        if(not user): 
            await message.reply(Config.language['cannot_find_user']); return db._close()

        db.ban_user(userID)

        try: 
            _b = await client.get_users(userID)
            _a = _b.id
            try: await client.send_message(_b.id, Config.language['you_got_banned_by'] % (message.from_user.mention))
            except: pass
            _b = _b.mention
        except: _b = userID
        await message.reply(Config.language['banned_user'] % (_b))
        logs.debug(f"{_a if not 0 else userID} has been banned by {message.from_user.id}")
        return db._close()
    
    reply_to = message.reply_to_message
    if(not reply_to):
        await message.reply(Config.language['incorrect_command_usage'])
        return db._close()

    if(not reply_to.entities):
        await message.reply(Config.language['incorrect_command_usage'])
        return db._close()
    if(not len(reply_to.entities) >= 2):
        await message.reply(Config.language['incorrect_command_usage'])
        return db._close()
    if(not reply_to.entities[1].user):
        await message.reply(Config.language['incorrect_command_usage'])
        return db._close()
    
    user = reply_to.entities[1].user

    if await Security.is_admin(user.id):
        await message.reply(Config.language['cannot_ban_an_admin']); return db._close()

    if user.id == message.from_user.id:
        await message.reply(Config.language['cannot_ban_urself']); return db._close()

    user = db.get_user(user.id)

    if(not user): 
        await message.reply(Config.language['cannot_find_user']); return db._close()

    db.ban_user(reply_to.entities[1].user.id)

    try: await client.send_message(reply_to.entities[1].user.id, Config.language['you_got_banned_by'] % (message.from_user.mention))
    except: pass

    await message.reply(Config.language['banned_user'] % (reply_to.entities[1].user.mention))
    logs.debug(f"{reply_to.entities[1].user.id} has been banned by {message.from_user.id}")
    db._close()
