#Write a function named geometry that takes the side length of a square and the radius of a circle. The function should print which shape has a larger perimeter/circumference and which shape has a larger area.
import math

def geometry(side, radius):
    square_perimeter = 4 * side
    square_area = side ** 2
    circle_circumference = 2 * math.pi * radius
    circle_area = math.pi * radius ** 2

    if square_perimeter > circle_circumference:
        print("The square has a larger perimeter than the circle.")
    elif square_perimeter < circle_circumference:
        print("The circle has a larger circumference than the square.")
    else:
        print("The square and the circle have the same perimeter/circumference.")
    if square_area >  circle_area:
        print("The square has a larger area than the circle.")
    elif circle_area > square_area:
        print("The circle has a larger area than the square")
    else:
        print("The square and the circle have the same area.")

geometry(3,5)