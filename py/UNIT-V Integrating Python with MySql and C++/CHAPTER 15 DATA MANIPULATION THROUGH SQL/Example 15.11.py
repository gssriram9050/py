import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("""DROP TABLE Appointment;""")
sql_command="""CREATE TABLE Appointment(rollno int primary key,Duty varchar(10),age int)"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Appointment(Rollno,Duty,age) VALUES("1","Prefect","17");"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Appointment(Rollno,Duty,age) VALUES("2","Secretary","16");"""
cursor.execute(sql_command)
#never forget this, if you want the changes to be saved:
connection.commit()
cursor.execute("SELECT student.rollno,student.sname,Appointment.Duty,Appointment.Age FROM student,Appointment where student.rollno=Appointment.rollno")
#print (cursor.description) to display the field names of the table
co=[i[0] for i in cursor.description]
print(co)
#Field informations can be read from cursor.description
result=cursor.fetchall()
for r in result:
    print(r)
