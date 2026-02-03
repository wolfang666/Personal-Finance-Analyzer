import sqlite3
from app.config import DB_PATH,SQLITE_TIMEOUT

def get_connection():
    return sqlite3.connect(
        DB_PATH,
        timeout=SQLITE_TIMEOUT,
        check_same_thread=False
    )