import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT GENDER,COUNT(GENDER) FROM Student GROUP BY GENDER HAVING COUNT(GENDER)>3")
result=cursor.fetchall()
co=[i[0] for i in cursor.description]
print(co)
print(result)
