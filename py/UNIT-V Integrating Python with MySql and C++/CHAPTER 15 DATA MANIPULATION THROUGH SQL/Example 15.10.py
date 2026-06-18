#code for executing query using input data
import sqlite3
#creates a database in RAM
con=sqlite3.connect("Academy.db")
cur=con.cursor()
cur.execute("DROP Table Person")
cur.execute("CREATE table Person(name,age,id)")
print("Enter 5 students names:")
who=[input() for i in range(5)]
print("Enter their ages respectively:")
age=[int(input()) for i in range(5)]
print("Enter their ids respectively:")
p_id=[int(input()) for i in range(5)]
n=len(who)
for i in range(n):
#This is the q-mark style:
    cur.execute("insert into person values (?,?,?)",(who[i],age[i],p_id[i]))
cur.execute("select * from person")
#Fetches all entries from table
print("Displaying All the Records From Person Table")
print(*cur.fetchall(),sep='\n')
