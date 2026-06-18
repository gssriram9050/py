#Program to sort the entire row by using a specified column.
#declaring multiple header files
import csv,operator
#One more way to read the file
data=csv.reader(open('C:\pyprg\sample8.csv'))
next(data)#(to omit the header)
#using operator module for sorting multiple columns
sortedlist=sorted(data,key=operator.itemgetter(1))#1 specifies we want to sort
                                                  #according to second column
for row in sortedlist:
    print(row)
