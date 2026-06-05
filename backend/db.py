import sqlite3

def get_db():
    return sqlite3.connect("users.db", check_same_thread=False)

def create_table():
    conn=get_db()
    cursor=conn.cursor()

    cursor.execute("""
               CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,email TEXT UNIQUE,password TEXT,google_id TEXT)""")

def insert_user(email, google_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO users (email, google_id) VALUES (?, ?)",
        (email, google_id)
    )

    conn.commit()
    conn.close()    