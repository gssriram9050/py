import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT Rollno, Sname FROM student WHERE (Average<60 OR Average>70)")
result=cursor.fetchall()
print(*result,sep="\n")
