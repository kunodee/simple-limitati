import json
from pyrogram import filters

class Config:

    # [+] BOT SETTINGS [+] #
    bot_token = ""
    api_id = ""
    api_hash = ""
    admins = []
    logs_enabled = True
    # [-] BOT SETTINGS [-] #

    # don't touch below this

    with open('language.json', encoding='utf-8') as fh:
        language = json.load(fh)

    if(bot_token == "" or api_id == "" or api_hash == "" or len(admins) == 0):
        print("Bot is not setupped yet. Please, open the config.py")
        quit(1)

    def cb_filter(data):
        async def func(flt, _, query):
            return flt.data == query.data
        return filters.create(func, data=data)

    in_chat = []