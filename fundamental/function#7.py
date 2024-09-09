def net_price(price, discount =0, tax = 0.08):
    return price * (1-discount) * (1+tax)

print(f"The price is: ${net_price(500,0.3)}")

import time

def countTime(end, start=0):
    for second in range(start, end+1):
        print(second)
        time.sleep(1)
    print("Time up!")

countTime(10)