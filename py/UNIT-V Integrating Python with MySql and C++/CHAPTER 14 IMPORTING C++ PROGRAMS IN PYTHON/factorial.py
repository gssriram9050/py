def fact(n):
    f=1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(1,n+1):
            f=f*i
        print(f)
