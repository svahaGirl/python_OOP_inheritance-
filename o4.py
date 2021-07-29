#!/usr/bin/python3
# inheritance example

# create parent class, also called super class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.") # have to have"f"

    def speak(self):
        print("I donot know what you mean.")

# create child class
class Cat(Pet):

    def __init__(self, name, age, color):
        super().__init__(name, age) # super means calling parent class
        self.color = color


    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.show()

c = Cat("Bill", 34, "Brown") # the cat inherites the class from the pet
c.show()
c.speak()
d = Dog("Jill", 22)
d.show()
d.speak()

f = Fish("LILLy", 3)
f.show()
f.speak() # it inherites the pet value