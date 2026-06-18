import csv
csv.register_dialect('myDialect',delimiter=',',skipinitialspace=True)
F=open('C:\pyprg\sample2.csv','r')
reader=csv.reader(F,dialect='myDialect')
for row in reader:
    print(row)
F.close()
