import math
def getDivisors(num):
    for n in range(2, num+1):
        if num% n == 0:
            print(n, end=" ")
            getDivisors(int(math.floor(num/n)))
            return

number= int(input("Enter a number:"))

print(f"The divisors for number {number} are: ", end="")
getDivisors(number)

print()
def writeVertical(num):
    if num < 10:
        print(num, end=" ")
    else:
        writeVertical(round(num/10))
        print(num%10, end=" ")

number2= int(input("Enter a number and press Enter:"))

writeVertical(number)
