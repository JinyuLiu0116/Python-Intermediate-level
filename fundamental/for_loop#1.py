for x in range(0,10):
    print(x)

for x in range(1,20):
    print(x*2)

for i in reversed(range(1,11)):
    print(i)
print("Happy new year!!!")

credit_card = "1254-2365-3254-5862"

for i in credit_card:
    if i =="-":
        continue
    else:
        print(i)

for i in credit_card:
    if i =="-":
        continue
    elif i =="8":
        print(f"Found nuber 8 at index position: {i}")
        break