class Student:
    mark1,mark2,mark3=45,91,71#class variable
    def process(self):#class method
        sum=Student.mark1+Student.mark2+Student.mark3
        avg=sum/3
        print("Total Marks =",sum)
        print("Average Marks =",avg)
        return
S=Student()
S.process()
