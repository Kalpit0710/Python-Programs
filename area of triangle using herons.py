import math
a=int(input("Enter side1 of triangle =a is:"))
b=int(input("Enter side2 of triangle =b is:"))
c=int(input("Enter side3 of triangle =c is:"))
s=(a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of given triangle is:",area)
