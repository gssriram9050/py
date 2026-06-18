#return statment
def usr_abs(n):
    if n>=0:
        return n
    else:
        return -n
#Now invoking the function
x=int(input("Enter a number : "))
print(usr_abs(x))
