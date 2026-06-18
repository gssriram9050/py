import csv
csv.register_dialect('myDialect',delimiter='|',skipinitialspace=True)
filename='C:\pyprg\ch13\sample8.csv'
with open(filename,'r') as csvfile:
    reader=csv.DictReader(csvfile,dialect='myDialect')
    for row in reader:
        print(dict(row))
csvfile.close()
