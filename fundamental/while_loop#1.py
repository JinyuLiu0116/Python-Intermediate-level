name = input("Enter your name:")

while name == "":
    print("You did not enter your name")
    name = print("Enter your name:")
print(f"Hello {name}")

age = int(input("Enter your age:"))

while age <=0:
    print("Age cannot less or equal to 0")
    age = int(input("Pleae enter your age:"))
print(f"Hello {name}, you are {age} years old")

gotOrder = False

while gotOrder == False:
    order = int(input("Pleae choose a order from 1-5:"))
    while not order>=1 and not order <=5:
        order= int(print("Please choose your order from 1-5:"))
    gotOrder= True
    
print(f"You have oredered number {order}")

food = print("Enter a food you like (q to quit):")

while not food=="q":
    print(f"You like {food}")
    food = print("Enter another food you like (q to quit):")

print("Bye!")
