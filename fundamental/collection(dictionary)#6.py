menu = {
    "pizza": 2.50,
    "nachos": 4.50,
    "popcorn": 3.00,
    "fries": 3.50,
    "chips": 2.00,
    "pretzel": 3.50,
    "soda": 1.00,
    "lemonade": 1.50
}

shipCart = []
total = 0
print("---------MENU----------")

for key, value in menu.items():
    print(f"| {key:13} ${value:.2f} |")

print("-----------------------")


while True:
    food = input("Select the item (q to quit):").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        shipCart.append(food)

print()
for food in menu:
    total+=menu.get(food)
    print(food,end=" ")

print()
print(f"Total is: ${total}")
