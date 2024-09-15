num=int(input("Enter a number between 1 and 10:"))
while(not num >=1 and not num <=10):
    print("Number must between 1 and 10.")
    num=int(input("Enter number again:"))

for k in range(3):
    for i in range(num):
        for j in range(num-i):
            print(" ",end="")
        for n in range(i):
            print("* ",end="")
        print()
    for i in range(num):
        for j in range(i):
            print(" ",end="")
        for n in range(num-i):
            print("* ",end="")
        print()
    print()

print()
for i in range(num):
    for j in range(i):
        print("*",end="")
    for n in range(num-i+1):
        print(" ",end="")
    for k in range(num-i):
        print(" ",end="")
    for l in range(i):
        print("*",end="")
    print()
for i in range(num):
    for j in range(num-i):
        print("*",end="")
    for n in range(i+1):
        print(" ",end="")
    for k in range(i):
        print(" ",end="")
    for l in range(num-i):
        print("*",end="")
    print()
print()

count = 9
for row in range(0,count+2,2):
    for space in range(0,count-row,2):
        print(" ", end="")
    for col in range(0,row-1):
        print("*", end="")
    print()
for row in range(0,count-1,2):
    for space in range(0,row+1,2):
        print(" ", end="")
    for col in range(0,count-2-row):
        print("*", end="")
    print()
