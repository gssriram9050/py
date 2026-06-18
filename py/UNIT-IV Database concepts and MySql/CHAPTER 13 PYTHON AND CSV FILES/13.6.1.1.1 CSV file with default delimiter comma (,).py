#importing csv
import csv
#opening the csv file which is in different location with read mode
with open('C:\pyprg\sample1.csv','r') as F:
#other way to open the file is f=('c:\pyprg\sample1.csv','r')
    reader=csv.reader(F)
#printing each line of the Data row by row
    for row in reader:
        print(row)
F.close()
