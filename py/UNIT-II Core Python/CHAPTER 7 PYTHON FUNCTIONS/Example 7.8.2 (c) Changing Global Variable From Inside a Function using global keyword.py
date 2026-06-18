x=0#global variable
def add():
    global x
    x=x+5#increment by 5
    print("Inside add() function x value is :",x)
add()
print("In main x value is :",x)
