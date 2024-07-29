import numpy as np

a = np.array([
    [1,2,3,10],
    [4,5,6,10],
    [7,8,9,10],
    [11,12,13,14]
])

# split array we have a 4 by 4 array
print(np.split(a, 4)) #output: 4 different array of each row of array a. we cannot split to 3 equal array

# horizontal
print(np.hsplit(a,2)) #output: two 4 by 2 arrays

# add array
b=[10,20,30,40] # simple python list

# append list b into array a
a1 = np.append(a,b) #output: a flatten array in one dimension
print(a1)

# append list b into array a withou changing a's shape
a2 = np.append(a,[b], axis=0) #output: 5 by 4 array, I don't know how the axis works
print(a2)

# insert 
a3 = np.insert(a, 1, b, axis=0)  #(array a, index position, list b, axis)
print(a3) #output: a 5 by 4 array with list b in the second row

a4 = np.insert(a, 1, b, axis=1) #axis=1 will add list b to the column
print(a4)