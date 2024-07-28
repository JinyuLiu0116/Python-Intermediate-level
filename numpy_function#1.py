import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(np.sin(a))
print(np.cos(a))
print(np.tan(a))
print(np.exp(a))# e to the power of 1, of 2, of 3, and so on
print(np.log(a)) 
print(np.sqrt(a))
print(np.power(a, 2))

# aggregate functions
print(a.sum()) #output: 45  the sum of all elements
print(a.max()) #output: 9  the highest value in the matrix
print(a.min()) #output: 1
print(a.mean()) #output: 5.0 (45/9) all the numbers sumed up and divided by the amount of numbers
print(np.median(a)) #output: 5.0  give the number in the middle of the array, if the amount is odd, 
#standard deviation|         will give the sum of middle two number divided by 2
print(np.std(a)) #output: 2.5199  how much on everage is each value deviating from the mean.

