a=-1
b=1
n=int(input("Enter no. of terms : "))
i=0
sum=0
Fibo=[]
while i<n:
    s=a+b
    Fibo.append(s)
    sum+=s
    a=b
    b=s
    i+=1
print("Fibonacci series upto "+str(n)+" terms is : "+str(Fibo))
print("The sum of Fibonacci series : ",sum)
