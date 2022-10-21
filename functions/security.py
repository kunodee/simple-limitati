from config import Config

class Security:

    async def is_admin(user_id: int = 0) -> bool:
        if(not user_id): return False

        if(user_id in Config.admins): return True
        return False