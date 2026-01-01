class Animal:
    def speak(self):
        print("Animal Speak.")
class Dog(Animal):
    def bark(self):
        print("Dog bark.")
class Cat(Animal):
    def meow(self):
        print("Cat meow")
c1 = Cat()
d1 = Dog()
c1.meow()
c1.speak()
d1.bark()
d1.speak()