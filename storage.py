import sqlite3

connection = sqlite3.connect("passwords.db")


cursor = connection.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                website TEXT,
                username TEXT,
                password TEXT NOT NULL)""")



