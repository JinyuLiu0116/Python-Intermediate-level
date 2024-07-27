import numpy as np
# manually fill array
a=np.array([
    [0,0,0],
    [0,0,0]
])
#(numbers of array, numbers of rows, numbers of columes)
a1=np.zeros((5,7,3))#zeros()function will fill array with 0s
print(a1)

#we can use full() function to specify value
a2=np.full((3,3),-1)
print(a2)
# empty will create np array with garbage values
a3=np.empty((2,6))
print(a3)

# my favorite random function!!!
a4=np.random.rand((10))*20
print(a4)