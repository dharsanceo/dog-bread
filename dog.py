class Dog:
    type = "Dog"   # class variable
    def __init__(self, name, breed):  # instance variables
        self.name = name
        self.breed = breed
d1 = Dog("Tommy", "Labrador")
d2 = Dog("Rocky", "Beagle")
print(Dog.type, d1.name, d1.breed)
print(Dog.type, d2.name, d2.breed)
