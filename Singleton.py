import threading
import sqlite3

class DBConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, db_path="app.db"):
        if cls._instance is None:
            with cls._lock:  # thread-safe
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self, db_path="app.db"):
        # Avoid re-initializing on every call
        if self._initialized:
            return
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)  # example DB
        self._initialized = True

    def execute(self, sql: str, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
        return cur.fetchall()


db1 = DBConnection("app.db")
db2 = DBConnection("app.db")

print(db1 is db2)  # True

db1.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT)")
db2.execute("INSERT INTO users VALUES(?, ?)", (1, "Yassine"))
print(db1.execute("SELECT * FROM users"))
