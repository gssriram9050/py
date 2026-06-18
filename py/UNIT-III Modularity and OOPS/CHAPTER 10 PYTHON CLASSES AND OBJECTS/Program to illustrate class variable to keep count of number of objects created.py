class Sample:
    num=0#class variable
    def __init__(self,var):
        Sample.num+=1
        self.var=var#instance variable
        print("The object value is =",self.var)
        print("The count of object created =",Sample.num)
S1=Sample(15)
S2=Sample(35)
S3=Sample(45)
