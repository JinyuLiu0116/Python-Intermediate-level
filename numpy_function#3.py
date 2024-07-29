import numpy as np

a = np.array([
    [1,2,3,10],
    [4,5,6,10],
    [7,8,9,10]
])
# two 3 by 4 matirces arrays
b = np.array([
    [10,20,30,100],
    [40,50,60,100],
    [70,80,90,100]
])

# when two numpy arrays have same shape, we can join them together
c = np.concatenate((a,b))
print(c) #output: a 6 by 4 matirces array with array a in the front follow by array b
print(np.shape(c)) #output: (6,4)

c2 = np.stack((a,b))
print(c2) #output: a three dimensional array with 2 lists, each list contain a 3 by 4 matirces array
print(np.shape(c2)) #output: (2,3,4)

# vstack() and hstack() functions stack arrays in different way
c3=np.hstack((a,b)) 
print(c3) #output: a 3 by 8 array, first row from a array appended by first roww from b array, same as row 2 and 3

c4=np.vstack((a,b))
print(c4) #output: same as np.stack() 
