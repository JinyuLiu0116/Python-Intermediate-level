num =-5
print("Number is postivate" if num >0 else "Number is negative")

num1=6
result="Even" if num1 % 2==0 else "Odd"
print(f"The {num1} is {result}")

a = float(input("Enter number a: ")) 
b = float(input("Enter number b: "))
max_num = a if a > b else b
print(f"The max number between {a} and {b} is {max_num}")
min_num = a if a < b else b
print(f"The min number between {a} and {b} is {min_num}")

age=int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Child"
print(f"Your are {age} years old, you are an/a {status}")

temperature = float(input("Enter today's temperature:"))
weather="Hot" if temperature >=35 else "Cold"
print(f"Today's {temperature} degree, it is {weather}")

user_role = "Admin"
access_level= "Full access" if user_role == "Admin" or user_role == "admin" else "limited access"
print(f"You have {access_level}")

