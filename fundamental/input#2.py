length=float(input("Enter the length of rectangle: "))
width=float(input("Enter the width of rectangle: "))
height=float(input("Enter the height of rectangle: "))

area = length * width
volume=length * width * height
print(f"The area is: {area}cm^2")
print(f"The volume if: {volume}cm^3")

math=float(input("Enter your score of math: "))
english=float(input("Enter your score of English: "))
science=float(input("Enter your score of Science: "))
CS=float(input("Enter your score of Computer Science: "))

average=(math+english+science+CS)/4
print(f"Your average is: {average}")
