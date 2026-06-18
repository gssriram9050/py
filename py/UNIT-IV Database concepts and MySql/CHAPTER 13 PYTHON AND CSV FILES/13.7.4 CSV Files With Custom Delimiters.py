import csv
info=[['SNO','Person','DOB'],
['1','Madhu','18/12/2001'],
['2','Sowmya','19/2/1998'],
['3','Sangeetha','20/3/1999'],
['4','Eshwar','21/4/2000'],
['5','Anand','22/5/2001']]
csv.register_dialect('myDialect',delimiter='|')
with open('C:\pyprg\ch13\dob.csv','w') as f:
    writer=csv.writer(f,dialect='myDialect')
    for row in info:
        writer.writerow(row)
f.close()
