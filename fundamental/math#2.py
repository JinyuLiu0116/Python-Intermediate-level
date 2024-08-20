import math

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference,2)}")

area = math.pi * pow(radius,2)
print(f"The area is: {round(area,2)}")

sideA=float(print("Enter the side A: "))
sideB=float(print("Enter the side B: "))

sideC=math.sqrt(pow(sideA, 2) + pow(sideB, 2))
print(f"The side C is: {sideC}")
