principle = 0
rate = 0
years = 0

while principle == 0:
    principle = float(input("Enter principle:"))
    while principle <=0:
        principle = float(input("Principle cannot less or equal to 0, please enter principle again:"))

while rate == 0:
    rate = float(input("Enter your rate:"))
    while rate <=0:
        rate = float(input("Rate cannot be less or equal to 0, please enter rate again:"))

while years == 0:
    years = int(input("Enter time in years:"))
    while years <=0:
        years = int(input("Time cannot be less or equal to 0 year, please enter again:"))

print(f"Your principle: ${principle}")
print(f"Your rate: {rate}%")
print(f"Your time: {years} year/years")

final_account= principle*pow((1+rate/100),years)
print(f"Balance after {years} year/s: ${final_account:.2f}")
