name = input("Enter your full name:")
if not name.find(" ")==-1:
    lengthOfString=len(name)-1
else:
    lengthOfString=len(name)
print(f"Your name has {lengthOfString} charters")

first_name = input("Enter your fist name:")
print("The name cannot include spicle charator" if not first_name.isalpha() else "Valid")
first_name=first_name.capitalize()
last_name = input("Enter your last name:")
last_name=last_name.capitalize()
full_name=first_name+" "+last_name

age=int(print("Enter your age:"))
if not age.is_integer():
    print("Age must be integer")
else:
    age=age

print(f"Your full name is: {full_name}")
print(f"Your are {age} years old")

phone_number=input("Enter your phone number:")
result=phone_number.count("_")
print(f"Phone number has {result} '_'")

phone_number=phone_number.replace("_","#")
print(f"Your new Phone number is: {phone_number}")

help(str)



