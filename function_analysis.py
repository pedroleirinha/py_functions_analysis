import matplotlib.pyplot as plt
import numpy as np

def calcFunction(x):
    return pow(x,2)+5

points = 5
min = points*-1
max = points+1

xpoints = np.arange(min, max)
ypoints = np.array([])

for num in np.sort(xpoints):
    newValue = calcFunction(num)
    ypoints = np.append(ypoints, newValue)
    
    print(f"x=>{num}, y=>{newValue}")


plt.plot(xpoints, ypoints)

zerosX = np.array([1, 2, 3])
zerosY = np.array([0, 0, 0])

plt.plot(zerosX, zerosY, 'o')

plt.show()
