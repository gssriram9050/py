str1=input("Enter a string : ")
str2=''
index=-1
for i in str1:
    str2+=str1[index]
    index-=1
print("The given string = {}\nThe Reversed string = {}".format(str1,str2))
if (str1==str2):
    print("Hence, the given string is Palindrome")
else:
    print("Hence, the given is not a palindrome")
