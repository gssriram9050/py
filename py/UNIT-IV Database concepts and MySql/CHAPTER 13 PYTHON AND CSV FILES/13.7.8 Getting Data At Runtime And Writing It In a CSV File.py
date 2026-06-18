import csv
with open('C:\pyprg\ch13\dynamicfile.csv','w') as f:
    w=csv.writer(f)
    ans='y'
    while (ans=='y'):
        name=input("Name?: ")
        date=input("Date of birth: ")
        place=input("Place: ")
        w.writerow([name,date,place])
        ans=input("Do you want to enter more y/n?: ")
    F=open('C:\pyprg\ch13\dynamicfile.csv','r')
    reader=csv.reader(F)
for row in reader:
    print(row)
F.close()
