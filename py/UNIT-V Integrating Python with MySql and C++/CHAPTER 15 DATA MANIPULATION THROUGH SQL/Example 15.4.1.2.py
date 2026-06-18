import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM student")
print("fetch one:")
res=cursor.fetchone()
print(res)
