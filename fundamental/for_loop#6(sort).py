import numpy as np

size=60

array=[np.random.randint(1,101) for i in range(size)]

print(array)
print()
for i in range(size-1):
    for j in range(size-1):
        if array[j]>array[j+1]:
            temp=array[j+1]
            array[j+1]=array[j]
            array[j]=temp
print(array)