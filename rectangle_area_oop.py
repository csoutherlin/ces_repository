class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def get_area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height
    
    def get_perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
if __name__ == "__main__":
        # Create a rectangle with width 5 and height 7
        rect_a = Rectangle(5, 7)    
        print("Rectangle a:")
        print(f"Area:      {rect_a.get_area()}")
        print(f"Perimeter: {rect_a.get_perimeter()}\n")

        # Create a rectangle with default width and height
        rect_b = Rectangle()
        rect_b.width = 10
        rect_b.height = 20
        print("Rectangle b:")
        print(f"Width:     {rect_b.width}")
        print(f"Height:    {rect_b.height}")
        print(f"Area:      {rect_b.get_area()}")
        print(f"Perimeter: {rect_b.get_perimeter()}")