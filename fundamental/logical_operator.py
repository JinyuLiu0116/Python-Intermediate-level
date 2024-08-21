temp = 25

if temp >0 and temp < 30:
    print("The temperature is good.")
else:
    print("The temperature is bad.")


if temp <=0 or temp >=30:
    print("The temperature is bad.")
else:
    print("The temperature is good.")

sunny=True

if not sunny:
    print("It is not sunny outside.")
else:
    print("It is sunny outside.")

num1=float(input("Enter number 1:"))
num2=float(input("Enter number 2:"))
if not num1==num2:
    print(f"{num1} not equals to {num2}")
else:
    print(f"{num1} equals to {num2}")

