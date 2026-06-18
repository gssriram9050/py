import csv
csv.register_dialect('myDialect',delimiter='|',quoting=csv.QUOTE_ALL)
with open('C:\pyprg\ch13\grade.csv','w') as csvfile:
    fieldnames=['Name','Grade']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames,dialect='myDialect')
    writer.writeheader()
    writer.writerows([{'Grade':'B','Name':'Anu'},
    {'Grade':'A','Name':'Beena'},
    {'Grade':'C','Name':'Tarun'}])
print("writing completed")
