import csv
#other way of declaring the filename
inFile='C:\pyprg\sample.csv'
F=open(inFile,'r')
reader=csv.reader(F)
#declaring array
arrayValue=[]
#displaying the content of the list
for row in reader:
    arrayValue.append(row)
    print(row)
F.close()
