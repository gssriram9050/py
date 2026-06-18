#sort a selected column given by user leaving the header column in
#descending order of value
import csv
#other way of declaring the filename
inFile='C:\pyprg\sample6.csv'
#opening the csv file which is in the same location of where the current python file
F=open(inFile,'r')
#reading the File with the help of csv.reader()
reader=csv.reader(F)
#skipping the first row(heading)
next(reader)
#declaring a list
arrayValue=[]
a=int(input("Enter the column number between 0 to 3:- "))
#sorting a particular column-cost
for row in reader:
    arrayValue.append(row[a])
arrayValue.sort(reverse=True)
for row in arrayValue:
    print(row)
F.close()
