fruits = ["apple", "orange", "banana", "cocount"]

for fruit in fruits:
    print(fruit,end=" ")

print()
print(len(fruits))

fruit = "orange"
if fruit in fruits:
    print(f"{fruit} is in the list of fruits.")
else:
    print(f"{fruit} is not in the list of fruits.")

fruits.append("watermelon")
print(fruits[4])
fruits[0] = "plum"

num = 1
for it in fruits:
    print(f"{num}: {it}")
    num += 1