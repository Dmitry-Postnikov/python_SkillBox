import sqlite3

with open('py1.sql', 'r', encoding='utf8') as sql_file:
    sql_script: str = sql_file.read()

with sqlite3.connect('database.db') as conn:
    cursor: sqlite3.Cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()