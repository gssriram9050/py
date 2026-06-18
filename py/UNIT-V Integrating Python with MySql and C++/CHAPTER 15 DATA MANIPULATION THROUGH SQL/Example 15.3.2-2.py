import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
student_data=[("BASKAR","C","M","75.2","1998-05-17"),("SAJINI","A","F","95.6","2002-11-01"),("VARUN","B","M","80.6","2001-03-14"),("PRIYA","A","F","98.6","2002-01-01"),("TARUN","D","M","62.3","1999-02-01")]
for p in student_data:
    format_str="""INSERT INTO Student(Rollno,Sname,Grade,gender,Average,birth_date) VALUES(NULL,"{name}","{gr}","{gender}","{avg}","{birthdate}");"""
    sql_command=format_str.format(name=p[0],gr=p[1],gender=p[2],avg=p[3],birthdate=p[4])
    cursor.execute(sql_command)
connection.commit()
connection.close()
print("RECORDS ADDED TO STUDENT TABLE")
