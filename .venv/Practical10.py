class Animal:
    def noise(self):
        pass

class Dog(Animal):
    def noise(self):
        print("Bark!")

class Human(Animal):
    def noise(self):
        print("Hi!")

class Horse(Animal):
    def noise(self):
        print("Neigh")

dog = Dog()
dude = Human()
horse = Horse()

dog.noise()
dude.noise()
horse.noise()