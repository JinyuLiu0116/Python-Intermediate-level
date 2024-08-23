num=int(input("Enter a number between 1 and 10:"))

while not num >=1 and not num <=10:
    print("Your numbe not in the range")
    num = int(input("Enter a number again, numer should between 1 and 10:"))

for i in range(num):
    for j in range(num):
        print("*",end="")
    print()
print()

for i in range(num):
    for j in range(num):
        print('A',end="")
    print()

for i in range(num):
    for j in range(i):
        print('*',end='')
    print()

for i in range(num):
    for n in range(num-i):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
    print()