import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT Rollno, Sname, Average FROM student WHERE(Average>=80 AND Average<=90)")
result=cursor.fetchall()
print(*result,sep="\n")
