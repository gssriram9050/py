import csv
row=['3','Meena','Bangalore']
with open('student.csv','r') as readFile:
    reader=csv.reader(readFile)
    lines=list(reader)#list()-to store each row of data as a list
    lines[3]=row
with open('student.csv','w') as writeFile:
#returns the writer object which converts the user data with delimiter
    writer=csv.writer(writeFile)
#writerows() method writes multiple rows to a csv file
    writer.writerows(lines)
readFile.close()
writeFile.close()
