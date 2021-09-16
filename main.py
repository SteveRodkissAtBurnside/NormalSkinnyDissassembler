import sqlite3


db = sqlite3.connect("Database/database.db")
sql = "CREATE TABLE IF NOT EXISTS Test (id INTEGER, name TEXT)"
c = db.cursor()
c.execute(sql)
db.commit()

db.close()