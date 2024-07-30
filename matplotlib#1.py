import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-100, 100, 201)#total 201 numbers
print(x)
x1 = np.arange(2,50,1)
print(x1) #same output as x

y= x**3+6*(x**2)-11*x+36 # x^3+6x^2-11x+36

plt.plot(x,y,'g*',label="cube")

y1=np.sin(x)*20000
plt.plot(x,y1,'b.',label="sin")

y2=np.log(x)*200000
plt.plot(x,y2,'r--',label="log")

plt.title("numpy functions",fontsize=18,color='blue')

plt.xlabel("X-axis",fontsize=13)
plt.ylabel("Y-axis",fontsize=13)

#y3=np.exp(x1)
#plt.plot(x1,y3)
plt.legend()
plt.show()
