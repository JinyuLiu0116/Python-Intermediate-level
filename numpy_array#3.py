import numpy as np
# manually
x=np.array([0,5,10,15,20,25,30])
#x**2 is x squared
y=x*2 - x**2  # we do the calculation with the vectors
print(y)
#give me all the values from 0 up until 1000 with the step size of 5
x1=np.arange(0,1001,5) #if use 1000, will up until 995, so need to set to 1001
print(x1)

# numpy functions
y=np.sin(x1)
print(y)
y1=np.cos(x1)
print(y1)
y2=np.tan(x1)
print(y2)

#how many value do I want to create evently distributed
x2=np.linspace(0,100, 11) # give me 10 values in between. because start from 0, we need 11
print(x2)