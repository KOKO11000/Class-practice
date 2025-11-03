class Animal:
    def __init__(self, *name):
        self.name = name

    def sound(self):
        print("This Animal make a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print(f"I'm {self.name} barking : Woof")

    
class Cat(Animal):
    def sound(self):
        super().sound()
        print(f"I {self.name} meow")
        
  
dog = Dog("Shuli")
dog1 = Dog("Dove")
dog2 = Dog("Lasi")
cat = Cat("putsi")
cat1 = Cat("Mutsi")
cat2 = Cat("Shaul")
animals: Animal = [dog, cat2,dog2, cat, cat1, cat2, dog1]

for i in animals:
    i.sound()

   