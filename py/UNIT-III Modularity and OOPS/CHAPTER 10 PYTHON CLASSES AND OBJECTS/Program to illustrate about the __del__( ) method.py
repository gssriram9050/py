class Sample:
    num=0
    def __init__(self,var):
        Sample.num+=1
        self.var=var
        print("The object value is =",self.var)
        print("The value of class variable is =",Sample.num)
    def __del__(self):
        Sample.num-=1
        print("Object with value %d is exit from the scope"%self.var)
S1=Sample(15)
S2=Sample(35)
S3=Sample(45)
del S1,S2,S3
