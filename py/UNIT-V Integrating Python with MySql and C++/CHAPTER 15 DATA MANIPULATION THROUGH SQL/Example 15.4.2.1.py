import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT DISTINCT (Grade) FROM student")
result=cursor.fetchall()
print(result)
