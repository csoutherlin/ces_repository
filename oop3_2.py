# Define the base class Shape
class Shape:
    def __init__(self, color):
        self.color = color

    def description(self):
        print(f"This shape is {self.color}")

# Define the subclass Square that inherits from Shape
class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def description(self):
        print(f"This square is {self.color} and has a side length of {self.side_length}")

# Create an instance of Shape
shape = Shape("red")
shape.description()

# Create an instance of Square
square = Square("blue", 5)
square.description()
