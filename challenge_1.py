#Input the lengths of all three sides of the triangle
import math


side1=float(input("Can you enter side1: " ))
side2=float(input("Can you enter side2: " ))
side3=float(input("Can you enter side3: " ))

#Triangle area calculation:

# 1) First we need to calculate s:
#s = (side1 + side2 + side3)/2
#s= (a/2)
a=[side1,side2,side3]
s=(sum(a))/2

# 2) Calculate the area:
#area = √(s(s-a)*(s-b)*(s-c))
#b= s(s-a)*(s-b)*(s-c)
#area= √(b)

b=s*(s-side1)*(s-side2)*(s-side3)
area=math.sqrt(b)

print(f"The area is: {area}")