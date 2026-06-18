import csv
Data=[['Fruit','Quantity'],['Apple','5'],['Banana','7'],['Mango','8']]
csv.register_dialect('myDialect',delimiter='|',lineterminator='\n')
with open('C:\pyprg\ch13\line.csv','w') as f:
    writer=csv.writer(f,dialect='myDialect')
    writer.writerows(Data)
f.close()
