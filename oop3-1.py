class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        print(f"Hello, my name is {self.first_name, self.last_name}")

#subclass
class Employee(Person):
    def __init__(self, first_name, last_name, employee_id):
        super().__init__(first_name, last_name)
        self.employee_id = (employee_id)

    def introduce(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}, and my employee ID: {self.employee_id}")

# Create an instance of Person
person = Person("John", "Doe")
person.introduce()

# Create an instance of Employee
employee = Employee("Jane", "Smith", "E123")
employee.introduce()