try: from pyrogram import Client, filters
except: print("Some libs are not installed, check out this: (pyrogram, tgcrypto)"); quit(1)
from config import Config
try: import logging, coloredlogs, colorama, time
except: print("Some libs are not installed, check out this: (logging, coloredlogs, colorama)"); quit(1)

app = Client(
    name="kunode",
    bot_token=Config.bot_token,
    api_id=Config.api_id,
    api_hash=Config.api_hash,
    plugins=dict(root="plugins")
)

logs = logging.getLogger("kunode")

LEVEL_STYLES = dict(
    info=dict(color='green'),
    warning=dict(color='yellow'),
    error=dict(color='red'),
)

coloredlogs.install(
    level='INFO',
    fmt=f"{time.strftime('%Y/%m/%d | %H:%M:%S')} | %(levelname)s » %(message)s",
    level_styles=LEVEL_STYLES
)

if __name__ == "__main__":
    app.run()
