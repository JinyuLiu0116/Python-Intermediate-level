def net_price(price, discount =0, tax = 0.08):
    return price * (1-discount) * (1+tax)

print(f"The price is: ${net_price(500,0.3)}")

import time
# default argument
def countTime(end, start=0):
    for second in range(start, end+1):
        print(second)
        time.sleep(1)
    print("Time up!")

countTime(10)

# keyword argument
def greeting(greet, title, firstName, lastName):
    print(f"{greet}, {title}.{firstName}{lastName}")

greeting("Hello", firstName="Jhon", lastName="James", title="Mr")

def phoneNumber(country, area, first, last):
    return f"+{country}({area})-{first}-{last}"

myNumber = phoneNumber(country=1, area=650, first=456, last=7890)
print(myNumber)
