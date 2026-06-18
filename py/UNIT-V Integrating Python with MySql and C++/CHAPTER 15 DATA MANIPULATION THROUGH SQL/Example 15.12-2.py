import sqlite3
import csv
#database name to be passed as parameter
conn=sqlite3.connect("Academy.db")
print("Content of the table before sorting and writing in CSV file")
cursor=conn.execute("SELECT * FROM Student")
for row in cursor:
    print(row)
#CREATING CSV FILE
d=open('C:\pyprg\sqlexcel.csv','w',newline='')
c=csv.writer(d)
cursor=conn.cursor()
cursor.execute("SELECT * FROM student ORDER BY GENDER DESC,SNAME")
#WRITING THE COLUMN HEADING
co=[i[0] for i in cursor.description]
c.writerow(co)
data=cursor.fetchall()
for item in data:
    c.writerow(item)
d.close()
print("sqlexcel.csv File is created open by visiting c:\pyprg\sqlexcel.csv")
conn.close()
