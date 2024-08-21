age=int(input("Enter your age: "))

if age>=18:
    print("You are now signed up!")
else:
    print("You must be 18+ to sign up!")


name=input("Enter your name:")
if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}.")

print("Please enter your scoar for you subjects.")
math=float(input("Math:"))
englis=float(input("English:"))
science=float(input("Science:"))
cs=float(input("Computer Science:"))

average=(math+englis+science+cs)/4

if average>=90 and average<=100:
    grade='A'
elif average>=80 and average< 90:
    grade='B'
elif average>=70 and average< 80:
    grade='C'
elif average>=60 and average< 70:
    grade='D'
else:
    grade='F'

print(f"Your average: {average}")
print(f"Your grade: {grade}")
