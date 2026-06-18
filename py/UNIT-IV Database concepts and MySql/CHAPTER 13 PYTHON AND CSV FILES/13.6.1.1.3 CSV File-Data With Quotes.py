import csv
csv.register_dialect('myDialect',delimiter=',',skipinitialspace=True)
f=open('C:\pyprg\quotes.csv','r')
reader=csv.reader(f,dialect='myDialect')
for row in reader:
    print(row)
