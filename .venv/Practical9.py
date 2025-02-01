#Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def getName(self):
        print(f"Name of animal::{self.name}.")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def getName(self):
        print(f"{self.name} is a cat")

cat1 = Cat("Philip")
cat2 = Cat("Roxi")

cat1.getName()
cat2.getName()