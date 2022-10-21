from functools import wraps
from config import Config
from functions.logs import logs

def only_admins(func):
    @wraps(func)
    async def wrapped(client, message):
        user = message.from_user
        if user.id not in Config.admins:
            return logs.debug(f"Unauthorized access to command for user {message.from_user.id}")
        return await func(client, message)
    return wrapped