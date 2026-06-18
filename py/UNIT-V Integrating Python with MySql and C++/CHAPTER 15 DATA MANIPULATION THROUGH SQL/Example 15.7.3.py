import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT SUM(AVERAGE) FROM student")
result=cursor.fetchall()
print(result)
