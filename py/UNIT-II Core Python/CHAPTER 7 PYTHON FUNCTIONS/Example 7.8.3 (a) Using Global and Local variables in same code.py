x=8#x is a global variable
def loc():
    global x
    y="local"
    x=x*2
    print(x)
    print(y)
loc()
