import numpy as np
# 3 by 4 matrix, total 12 elements
a = np.array([
    [1,2,3,10],
    [4,5,6,10],
    [7,8,9,10]
])

#shape manipulate functions
# need to keep same amount of element when apply reshape function
a = a.reshape((2,6)) 
print(a) #output: 2 rows, 6 columns
a=a.reshape((6,2))
print(a) #output: 6 rows, 2 columns
a=a.reshape((2,3,2)) # reshape into a three dimensional array
print(a) #output: 2 lists with 3 rows and 2 columns

# flat function can flatten an array to one dimensional array
print(a.flatten())

# transpose function  can swap the shape of the array
# array a has 3 by 4
print(a.transpose()) #output: a 4 by 3 array

# flat iterator
#  a.flat, the flat is not a function but the flattened version of this array
#  and we can iterate it 
for x in a.flat:  # important way to read elements in numpy array
    print(x) # output: all the values in different line

