fruits = ["apple", "orange", "banana", "pear"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "pork", "beef"]

food = [fruits, vegetables, meats]

print(food)
food[0][2]="watermelon"
print(food[0])
food[1][0]="eggplant"
print(food[1])
food[2][1]="lamb"
print(food[2])

for i in food:
    for j in i:
        if not j == i[len(i)-1]:
            print(j, end=", ")
        else:
            print(j, end=". ")
    print()