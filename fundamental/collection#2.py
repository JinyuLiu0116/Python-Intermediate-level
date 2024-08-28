import numpy as np

size = 20

array=[None]*20

for it in array:
    print(it,end=" ")
print()
for i in range(size):
    array[i]=np.random.randint(1,21)
    print(array[i],end=" ")
print()

min=20
max=1
sum=0
for i in range(size):
    sum+=array[i]
    if min>array[i]:
        min=array[i]
    if max<array[i]:
        max=array[i]
print(f"The sum of the array:{sum}\nThe min value is:{min}\nThe max valuse is:{max}")