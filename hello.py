import csv


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def introduce(self):
        print(f"Hi I am {self.name} and I am a {self.colour} {self.species}")


dog = Pet("Buddy", "Dog")
cat = Pet("Whiskers", "Cat")
cat.colour = "White"
cat.introduce()
dog.name = "Max"
dog.colour = "Brown"
dog.introduce()
