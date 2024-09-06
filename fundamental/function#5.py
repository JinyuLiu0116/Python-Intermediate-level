#Imagine a circle and two squares: a smaller and a bigger one. 
# For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.
#Create a function, that takes an integer (radius of the circle) and returns the difference of the areas of the two squares.

import math

#first need user input a number for the radius

def insideSquare(radius):
    length = math.sqrt(2)*radius
    area = pow(length, 2)
    return area
def outsideSquare(radius):
    length = 2 * radius
    area = pow(length, 2)
    return area
def diff_Area(area1, area2):
    if area1 >= area2:
        return round(area1-area2)
    else:
        return round(area2-area1)
    
radius = float(input("Enter radius:"))
while radius <= 0:
    print("Radius cannnot less or equalt to 0")
    radius = float(input("Enter radius again:"))

area1=insideSquare(radius)
area2=outsideSquare(radius)
different=diff_Area(area1,area2)
print(f"The different is:{different}")