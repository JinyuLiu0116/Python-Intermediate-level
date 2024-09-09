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
