import csv
row=['6','Sajini','Madurai']
with open('student.csv','a') as CF:#append mode to add data at the end
    writer=csv.writer(CF)
    writer.writerow(row)#writerow() method write a single row of data in file
CF.close()
