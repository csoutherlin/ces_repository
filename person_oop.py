class Person: 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        """Print a brief introduction of the person."""
        print(f"Hello! My name is {self.name}. I am {self.age} years old and identify as {self.gender}.")

# Example usage:
if __name__ == "__main__":
    person1 = Person("Alice", 30, "female")
    person1.introduce()

    person2 = Person("Bob", 25, "male")
    person2.introduce()        


       
    
