class Animal:
    def __init__(self, name):
        self.name=name
        self.has_onwer = True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is asleep")
    def play(self):
        print(f"{self.name} is playing with its onwer")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}: Meow~")

class Hamster(Animal):
    def speak(self):
        print(f"{self.name}: Squeek Squeek!")

dog = Dog("Tigeey")
dog.eat()
dog.sleep()
dog.play()
dog.speak()

print()
cat = Cat("Garfield")
cat.eat()
cat.sleep()
cat.play()
cat.speak()

print()
hamster = Hamster("ikura")
hamster.eat()
hamster.sleep()
hamster.play()
hamster.speak()
