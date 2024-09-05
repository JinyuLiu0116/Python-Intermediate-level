import numpy as np

def fillList(list, size):
    list.extend(np.random.randint(1,size+1) for i in range(size))

def transf(list, size):#if even, decrease by 2. if odd, increase by 2
    for index in range(size):
        if list[index]%2==0:
            list[index]-=2
        if not list[index]%2==0:
            list[index]+=2

repectNum = int(input("Please enter a number of times you want to repect:"))
size=int(input("Please enter the size of the lise:"))

list=[]

fillList(list,size)
print(list)
print()

for repect in range(repectNum):
    transf(list, size)

print(list)



