count=0
n=int(input("Enter no. of employees : "))
print("No. of Employees",n)
salary=[]
for i in range(n):
    print("Enter Monthly Salary of Employee {} Rs. :".format(i+1))
    s=int(input())
    salary.append(s)
for j in range(len(salary)):
    annual_salary=salary[j]*12
    print("Annual Salary of Employee {} is : Rs. {}".format(j+1,annual_salary))
    if annual_salary >= 100000:
        count=count+1
print("{} Employees out of {} employees are earning more than Rs. 1 Lakh per annum".format(count,str(n)))
