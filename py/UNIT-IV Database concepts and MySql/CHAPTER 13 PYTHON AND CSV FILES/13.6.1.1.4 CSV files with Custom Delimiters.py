import csv
csv.register_dialect('myDialect',delimiter='|')
with open('C:\pyprg\sample4.csv','r') as f:
    reader=csv.reader(f,dialect='myDialect')
    for row in reader:
        print(row)
f.close()
