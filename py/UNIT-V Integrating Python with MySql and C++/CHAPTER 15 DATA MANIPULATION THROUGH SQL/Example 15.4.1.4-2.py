import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM student")
print("fetching first 3 records:")
result=cursor.fetchmany(3)
print(*result,sep="\n")#* is used for unpacking a tuple
