#Program to illustrate the use of nested if statement
m1=int(input("Enter mark in first subject : "))
m2=int(input("Enter mark in second subject : "))
avg=(m1+m2)/2
if avg>=80:
    print("Grade : A")
elif avg>=70 and avg<80:
    print("Grade : B")
elif avg>=60 and avg<70:
    print("Grade : C")
elif avg>=50 and avg<60:
    print("Grade : D")
else:
    print("Grade : E")
