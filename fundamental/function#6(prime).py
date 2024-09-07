import math
def checkPrime(num):
    if num <2:
        return False
    for n in range(2, math.isqrt(num)+125):
        if num % n == 0:
            return False
    return True
def print_result(num):
    if checkPrime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

while True:
    number=int(input("Enter number (0 = exit) and press Enter:"))
    if number == 0:
        break
    print_result(number)
