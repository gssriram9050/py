#Program to illustrate the use of 'in' and 'not in' in if statement
ch=input("Enter a character : ")
#to check if the letter is vowel
if ch in ('a','A','e','E','i','I','o','O','u','U'):
    print(ch,'is a vowel')
#to check if the letter typed is not 'a' or 'b' or 'c'
if ch not in ('a','b','c'):
    print(ch,'the letter is not a/b/c')
