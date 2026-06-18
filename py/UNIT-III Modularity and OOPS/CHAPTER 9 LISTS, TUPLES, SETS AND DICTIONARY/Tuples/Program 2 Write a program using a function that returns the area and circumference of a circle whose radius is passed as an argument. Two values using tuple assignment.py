pi=3.14
def Circle(r):
    return (pi*r*r,2*pi*r)
radius=float(input("Enter the Radius : "))
(area,circum)=Circle(radius)
print("Area of the circle =",area)
print("Circumference of the circle =",circum)
