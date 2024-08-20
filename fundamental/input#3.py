item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} {item}/s.")
print (f"Your total is: ${total}")


name=input("What is your name?: ")
tital=input("What is your job tital?: ")
position=input("What is your position?: ")
maxHour=float(input("What is your maximun weakly working hours?: "))
hourlySalary=float(input("What is your hourly salary?: "))
workHours=float(input("How many hours want to work?: "))

check=hourlySalary * workHours * 2

print(f"Hello {name}.\nYou are {tital} {position}.\nYou can work {maxHour} hours a weak.")
print(f"You choose to work {workHours} hours and your hourly salary is: ${hourlySalary}")
print(f"You will recive your bill check each two weaks with {check} dollars.")