import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
sql_command="""CREATE TABLE Student(Rollno INTEGER PRIMARY KEY,Sname VARCHAR(20),Grade CHAR(1),gender CHAR(1),Average DECIMAL(5,2),birth_date DATE);"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Student(Rollno,Sname,Grade,gender,Average,birth_date) VALUES(NULL,"Akshay","B","M","87.8","2001-12-12");"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Student(Rollno,Sname,Grade,gender,Average,birth_date) VALUES(NULL,"Aravind","A","M","92.50","2000-08-17");"""
cursor.execute(sql_command)
#never forget this, if you want the changes to be saved:
connection.commit()
connection.close()
print("STUDENT TABLE CREATED")
