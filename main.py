import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
        name INTEGER,
        sex INTEGER, 
        old INTEGER,
        score INTEGER
        )''')