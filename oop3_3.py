class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def drive(self):
        print(f"The vehicle driving")

class Car(Vehicle):
    def __init__(self):
        super().__init__(wheels=4)    

    def drive(self, speed=None):
        if speed:
            print(f"The car is driving at {speed} mph")
        else:
            print(f"The car is driving")

# Create an instance of Vehicle
vehicle = Vehicle(2)
vehicle.drive()

# Create an instance of Car
car = Car()
car.drive()
car.drive(speed=60)            