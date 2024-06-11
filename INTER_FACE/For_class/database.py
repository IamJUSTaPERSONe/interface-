import sqlite3

connect = sqlite3.connect('database.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXIST User (
email TEXT PRINARY KEY,
username TEXT NOT NULL,
password INTEGER NOT NULL
)
''')







connect.commit()
connect.close()
