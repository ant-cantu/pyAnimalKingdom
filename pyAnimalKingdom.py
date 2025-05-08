# Project is created to demonstrate an understanding of Inheritance , 
# Method Overidding, and Polymoprhism
# ------------------------------------

# Class Defintions

# Parent Class (Base/Superclass)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("This animal makes a sound.")

# Child Class (Subclass)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog") # Inherit base class __init__ and pass arguments
        self.breed = breed

    def make_sound(self): # Override base class make_sound
        print("Woof!")

    def growl(self):
        print("Grrrrr.")

# Child Class (Subclass)
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Cat") # Inherit base class __init__ and pass arguments
        self.breed = breed

    def make_sound(self): # Override base class make_sound
        print("Meow!")

    def purr(self):
        print("Purrrrrr.")

# End Class Defintions
# ************************************************

# Implementation

# Create objects of the classes defined above.
callie = Dog("Callie", "Husky")
opie = Cat("Opie", "Long Hair")
ruhn = Cat("Ruhn", "Short Hair")

# Add objects to a list
animals = [callie, opie, ruhn]

# Loop through each object in the list and call make_sound()
for animal in animals:
    animal.make_sound()

    if isinstance(animal, Dog):
        animal.growl()
    elif isinstance(animal, Cat):
        animal.purr()


# Create another object and add it to the end of the list
cruise = Dog("Cruise", "Great Dane")
animals.append(cruise)
print("\nAdded a new animal.\n")

# Loop through the list again
for animal in animals:
    animal.make_sound()

    if isinstance(animal, Dog):
        animal.growl()
    elif isinstance(animal, Cat):
        animal.purr()