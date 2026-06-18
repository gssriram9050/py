str1=input("Enter a string : ")
str2="aAeEiIoOuU"
v,c=0,0
for i in str1:
    if i in str2:
        v+=1
    elif i.isalpha():
        c+=1
print("The given string contains {} vowels and {} consonants".format(v,c))
