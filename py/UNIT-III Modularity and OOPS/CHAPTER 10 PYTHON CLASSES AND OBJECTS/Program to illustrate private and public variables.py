class Sample:
    n1=12
    __n2=14
    def display(self):
        print("Class variable 1 =",self.n1)
        print("Class variable 2 =",self.__n2)
S=Sample()
S.display()
print("Value 1 =",S.n1)
print("Value 2 =",S.__n2)
