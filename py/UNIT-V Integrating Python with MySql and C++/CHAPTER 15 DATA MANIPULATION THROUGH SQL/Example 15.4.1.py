#save the file as “sql_Academy_query.py”
import sqlite3
connection=sqlite3.connect("Academy.db")
crsr=connection.cursor()
#execute the command to fetch all the data from the table Student
crsr.execute("SELECT * FROM Student")
#store all the fetched data in the ans variable
ans=crsr.fetchall()
#loop to print all the data
for i in ans:
    print(i)
