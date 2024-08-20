operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Cannot divide by 0.")
    else:
        result = round(num1 / num2, 2)
else:
    print(f"Invalid input operator: {operator}")

print(f"{num1} {operator} {num2} = {result}")