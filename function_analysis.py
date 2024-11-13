import math
import matplotlib.pyplot as plt
import numpy as np

# coeff = [1, 5, -10]
# print(f"roots: {np.polynomial.polynomial.polyroots(coeff)}")


def calcFunction(a, b, c, x):
    first = a*pow(x,2) 
    second = b*x 
    third = c 
    
    return first + second + third

def findZeros(a, b, c):
    d = b**2-(4*a*c) # discriminant
    
    zeros = np.array([])
    if d < 0:
        print ("This equation has no real solution")
    elif d == 0:
        x = (-b+math.sqrt(d))/(2*a)
        zeros = np.append(zeros, x)
        print ("This equation has one solutions: ", x)
    else:
        x1 = ((-b)+math.sqrt(d))/(2*a)
        x2 = ((-b)-math.sqrt(d))/(2*a)
        zeros = np.append(zeros, [x1,x2])
        print ("This equation has two solutions: ", x1, " and", x2)
    
    return zeros

points = 20
min = points*-1
max = points

a = 1
b = 5
c = -10

xpoints = np.arange(min, max, 0.1)
ypoints = np.array([])


for num in np.sort(xpoints):
    newValue = calcFunction(a,b,c,num)
    ypoints = np.append(ypoints, newValue)
    
    print(f"x=>{num}, y=>{newValue}")


plt.plot(xpoints, ypoints)

zerosX = findZeros(a,b,c)
print(f"The zeroes of the function are: {zerosX}")
zerosY = np.array([0, 0])

plt.plot(zerosX, zerosY, 'o')
plt.show()
