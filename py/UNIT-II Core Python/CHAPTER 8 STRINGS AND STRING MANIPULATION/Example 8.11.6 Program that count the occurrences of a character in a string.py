def count(s,c):
    c1=0
    for i in s:
        if i==c:
            c1+=1
    return c1
str1=input("Enter a String : ")
ch=input("Enter a character to be searched : ")
cnt=count(str1,ch)
print("The given character {} is occurs {} times in the given string".format(ch,cnt))
