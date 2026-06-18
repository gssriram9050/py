class Odd_Even:
    def check(self,num):
        if num%2==0:
            print(num,"is Even number")
        else:
            print(num,"is Odd number")
n=Odd_Even()
x=int(input("Enter a value : "))
n.check(x)
