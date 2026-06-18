import sqlite3
import csv
#CREATING CSV FILE
d=open('C:/pyprg/sql.csv','w',newline='')
c=csv.writer(d)
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM student ORDER BY GENDER DESC,SNAME")
#WRITING THE COLUMN HEADING
co=[i[0] for i in cursor.description]
c.writerow(co)
data=cursor.fetchall()
for item in data:
    c.writerow(item)
d.close()
#Reading the CSV File
with open('C:/pyprg/sql.csv','r') as fd:
    for line in fd:
        line=line.replace("\n","")
        print(line)
cursor.close()
connection.close()
