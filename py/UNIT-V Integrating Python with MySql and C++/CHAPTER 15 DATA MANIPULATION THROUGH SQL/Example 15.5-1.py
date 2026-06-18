import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM student where NOT Grade='A' and NOT Grade='B'")
result=cursor.fetchall()
print(*result,sep="\n")
