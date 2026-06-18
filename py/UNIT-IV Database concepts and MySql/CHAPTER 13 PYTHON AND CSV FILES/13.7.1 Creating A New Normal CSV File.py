import csv
csvData=[['Student','Age'],['Dhanush','17'],['Kalyani','18'],['Ram','15']]
with open('C:\pyprg\ch13\Pupil.csv','w') as CF:
    writer=csv.writer(CF)#CF is the file object
    writer.writerows(csvData)#csvData is the List name
CF.close()
