#import math

#def triangle_area_heron(a, b, c):
#    s = (a + b + c) / 2
#    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#    return area

# Inputting the values of the three sides of the triangle
#a = float(input("Enter the first side length of the triangle: "))
#b = float(input("Enter the second side length of the triangle: "))
#c = float(input("Enter the third side length of the triangle: "))

# Printing the result
#print("The area of the triangle is", triangle_area_heron(a, b, c))

#---------------------------------------------------------------------

#def square_area(l):
#  square_area = l  
#l = float(input("Enter length: "))
#print(f"The area of square is {l * l}.")


#-------------------------------------------------------------------------
def findArea(r):
    PI = 3.14
    return PI * (r*r)
print("Area of circle = %.6f" % findArea(6))

