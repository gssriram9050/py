import csv
#opening the csv file which is in different location with read mode
f=open('C:\pyprg\ch13\sample5.csv','r')
#reading the File with the help of csv.reader()
readFile=csv.reader(f)
#printing the selected column
for col in readFile:
    print(col[0],col[3])
f.close()
