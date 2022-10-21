import time
import sqlite3
from functions.logs import logs

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()

    def get_user(self, user_id):
        self.cur.execute(f"SELECT * FROM users WHERE user_id == {user_id}")
        result = self.cur.fetchone()
        if(not result): return False
        return result

    def get_users(self):
        rows = self.cur.execute("SELECT * FROM users").fetchall()
        logs.debug(f"Loaded ({len(rows)}) user/s from the database")
        return rows

    def add_user(self, user):
        cur = self.conn.cursor()
        if(not self.get_user(user.id)):
            cur.execute(f"INSERT INTO users(user_id, start_date, is_banned) VALUES({user.id}, {int(time.time())}, 'False')")
            logs.debug(f"{user.id} is now in the database.")
            self._commit()

    def is_banned(self, user) -> bool:
        user = self.get_user(user.id)
        if(not user): return False
        if(user[3] == "True"): return True
        return False

    def ban_user(self, userid):
        self.cur.execute(f"UPDATE users SET is_banned = 'True' WHERE user_id = {userid}")
        self._commit()
    
    def unban_user(self, userid):
        self.cur.execute(f"UPDATE users SET is_banned = 'False' WHERE user_id = {userid}")
        self._commit()

    def get_bans(self):
        rows = self.cur.execute("SELECT * FROM users WHERE is_banned = 'True'").fetchall()
        logs.debug(f"Loaded ({len(rows)}) user/s from the database")
        return rows

    def _commit(self):
        self.conn.commit()

    def _close(self):
        self.conn.commit()
        self.conn.close()