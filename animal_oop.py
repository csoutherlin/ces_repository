class Animal: 
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def eat(self, food):
        """Simulates the animal eating"""
        print(f"{self.name} is eating {food}.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

# Example usage:
if __name__ == "__main__":
    # Create an instance of Animal
    my_pet = Animal("Fluffy", "Cat")

    # Get and print the name and species
    print(f"Name: {my_pet.get_name()}")
    print(f"Species: {my_pet.get_species()}")

    # Simulate eating and sleeping
    my_pet.eat("fish")
    my_pet.sleep()