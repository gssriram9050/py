import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT gender,count(gender) FROM student Group BY gender")
result=cursor.fetchall()
print(*result,sep="\n")
