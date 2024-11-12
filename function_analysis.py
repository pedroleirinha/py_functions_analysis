import math 
import matplotlib.pyplot as plt
import numpy as np

def calcFunction(x):
    return x**3+6*x**2-5*x-6


min = -50
max = 50

xpoints = np.arange(min, max)
ypoints = np.array([])

for num in np.sort(xpoints):
    newValue = calcFunction(num)
    ypoints = np.append(ypoints, newValue)

    #print(f"x=>{num}")
    print(f"x=>{num} <=> y=> {newValue}")


plt.plot(xpoints, ypoints)
plt.show()
