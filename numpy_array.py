import numpy as np

a=np.array([1,2,3,4])
b=np.array([6,7,8,9])

print(a[0])
print(b[1])
#numpy array will add index position
print(a+b)

m=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])
# shape shows rows and columns in form of (r,c)
print(m.shape)

x=[1,2,3,4]
y=[5,6,7,8]
#nomal array will combine when added
# numpy array is vector?
print(x+y)