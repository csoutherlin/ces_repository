# Define the base class Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Define the subclass Square that inherits from Rectangle
class Square(Rectangle):
    def __init__(self, side_length):
        self.side_length = side_length
        super().__init__(side_length, side_length)

    def perimeter(self):
        return (4 * self.side_length)

# Create an instance of Rectangle
rectangle = Rectangle(4, 5)
print(f"The area of the rectangle is {rectangle.area()}")

# Create an instance of Square
square = Square(3)
print(f"The area of the square is {square.area()}")
print(f"The perimeter of the square is {square.perimeter()}")

     