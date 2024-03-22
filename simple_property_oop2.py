class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        """Returns the diameter of the circle (twice the radius)"""
        return 2 * self.radius
    
# Create an instance of the Circle class with a radius of 5
circle = Circle(radius=5)

#Display the diameter
print(f"The diameter of the circle is: {circle.diameter}")