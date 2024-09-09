class Car:
    def __init__(self, model, year, color, for_sale):
        self.model=model
        self.year=year
        self.color=color
        if for_sale == 'Y':
            self.for_sale = True
        elif for_sale == 'N':
            self.for_sale = False
        else:
            self.for_sale = False
    def drive(self):
        print(f"You drive the {self.model}")
    def stop(self):
        print(f"You stop the {self.model}")

name=input("Please enter your name:")

model=input(f"Hello {name}, Please enter the brand of your car:")

year=int(input("Please enter the year:"))

color=input("Please enter the color:")

sale=(input("Your car for sale(Y/N):")).strip().upper()

car1 = Car(model, year, color, sale)

print(f"Onwer name: {name}")
print(f"Brand: {car1.model}")
print(f"Year: {car1.year}")
print(f"Color: {car1.color}")
if car1.for_sale:
    print(f"{name}'s {car1.model} {car1.year} is for sale")
else:
    print(f"{name}'s {car1.model} {car1.year} is not for sale")

