import csv
filename='C:\pyprg\sample8.csv'
input_file=csv.DictReader(open(filename,'r'))
for row in input_file:
    print(dict(row))#dict() to print data
