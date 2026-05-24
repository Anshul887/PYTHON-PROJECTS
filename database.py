import sqlite3

conn = sqlite3.connect("database/expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    amount REAL,
    category TEXT,
    date TEXT
)
""")

conn.commit()

def execute_query(query, params=()):
    conn.execute(query, params)
    conn.commit()

def fetch_query(query, params=()):
    cursor = conn.execute(query, params)
    return cursor.fetchall()
