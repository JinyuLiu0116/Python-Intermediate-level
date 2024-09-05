import numpy as np

def fillArray(array,size):
    array.extend(np.random.randint(1,51) for i in range(size))

def sortArray(array,size):
    temp = 0
    for i in range(size-1):
        for j in range(size-1):
            if array[j] > array[j+1]:
                temp=array[j+1]
                array[j+1]=array[j]
                array[j]=temp
                
size = 20
array=[]

fillArray(array,size)
print(array)

sortArray(array,size)
print(array)