class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("width must be a positive number")
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("height must be a positive number")
        
    @property
    def area(self):
        return self._width * self._height
    
rectangle = Rectangle(10, 5)
print(f"Area: {rectangle.area}")
rectangle.width = 20
rectangle.height = 2
print(f"Area: {rectangle.area}")

