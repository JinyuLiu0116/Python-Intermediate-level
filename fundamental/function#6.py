import numpy as np
size=300
def getAverage(x, y):
    return (x+y)/2
     
def testAverage():
    for i in range(size):
        x = np.random.randint(0,size)
        y = np.random.randint(0,size)
        ave=getAverage(x,y)
        print(f"The average of {x} and {y} is: {ave}")


testAverage()