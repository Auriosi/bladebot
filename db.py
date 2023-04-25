import sqlite3
import asyncio
connection = None
try:
    connection = sqlite3.connect("database.sqlite")
    print("Successfully connected to the database!", file=open("logs.txt", "a"))
    print("Successfully connected to the database!")
except sqlite3.Error as e:
    print("An error occured while connecting to the database: " + str(e), file=open("logs.txt", "a"))
    print("An error occured while connecting to the database: " + str(e))
    exit(-1)

async def commitloop():
    while True:
        connection.commit()
        await asyncio.sleep(2)