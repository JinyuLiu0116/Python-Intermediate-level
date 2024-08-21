weight = float(input("Enter your weight:"))
unit = input("Kilograms or Pounds? (K or L):")

if unit=='K' | unit=='k':
    weight *= 2.205
    unit="LBS"
    print(f"Your weight is: {round(weight,1)} {unit}.")
elif unit =='L' | unit=='l':
    weight /= 2.205
    unit="Kgs"
    print(f"Your weight is: {round(weight,1)} {unit}.")
else:
    print(f"{unit} was not valid.")

