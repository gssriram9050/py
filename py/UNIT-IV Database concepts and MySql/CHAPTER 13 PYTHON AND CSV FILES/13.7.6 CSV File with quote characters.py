import csv
csvData=[['SNO','Items'],['1','Pen'],['2','Book'],['3','Pencil']]
csv.register_dialect('myDialect',delimiter='|',quotechar='"',quoting=csv.QUOTE_ALL)
with open('C:\pyprg\ch13\quote.csv','w') as csvFile:
    writer=csv.writer(csvFile,dialect='myDialect')
    writer.writerows(csvData)
print("writing completed")
csvFile.close()
