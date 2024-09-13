class Animal:
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.name
    def setName(self, name):
        self.name=name
    def eat(self):
        print(f"{self.getName()} is Eating")
    def sleep(self):
        print(f"{self.getName()} is asleep")
class Pray(Animal):
    def flee(self):
        print(f"{self.getName()} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.getName()} is hunting")

class Rabbit(Pray):
    pass

class Hawk(Predator):
    pass

class Fish(Pray, Predator):
    pass

rabbit = Rabbit("Rabeen")
hawk = Hawk("Stone")
fish = Fish("Blade")

rabbit.flee()
rabbit.eat()
rabbit.sleep()

print()
hawk.hunt()
hawk.eat()
hawk.sleep()

print()
fish.flee()
fish.hunt()
fish.eat()
fish.sleep()
