import math
num = int(input("Enter a number:"))
n1=0
n2=1
n3=0
print(n1,end=" ")
for i in range(num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
print()

k1=0
k2=1
k3=0
print(f"{k1} {k2}",end=" ")
for j in range(num):
    k3=k1*k2+k2
    k1=k2
    k2=k3
    print(k3,end=" ")
print()

armstrong=(input("Enter a interge:"))
while(int(armstrong)<0):
    print("Cannot have negative number.")
    armstrong=(input("Enter a interge:"))
digit=len(armstrong)
armstrong=int(armstrong)
temp=armstrong
result=0
for i in range(digit):
    x=temp % 10
    y=pow(x,digit)
    result+=y
    temp/=10
    temp=math.floor(temp)
if result == armstrong:
    print(f"The number of {armstrong} is a Armstrong number.")
else:
    print(f"The number {armstrong} is not a Armstrong number.")
