import sqlite3

def init_db():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE NOT NULL
        ) 
    """)
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect("todo.db")
    conn.row_factory =sqlite3.Row
    return conn
