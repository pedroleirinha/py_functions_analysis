import math
import matplotlib.pyplot as plt
import numpy as np
from function_class import Function

# coeff = [1, 5, -10]
# print(f"roots: {np.polynomial.polynomial.polyroots(coeff)}")

def plotFunction(function, showZeros, func_name_label = "f", plotColor = "blue"):
    
    plt.xlim(-5, 10)
    plt.ylim(-5, 10)
    
    plt.plot(function.xpoints, function.ypoints, color=plotColor, label=f"{func_name_label}(x)={showFunction(func)}")
    plt.legend(fontsize=14)
    
    # zerosX = findZeros(a,b,c)
    
    if showZeros:
        print(f"The zeroes of the function are: {function.zerosX}")
        zerosY = np.array(np.zeros(len(function.zerosX)))
        
        plt.plot(list(function.zerosX), zerosY, 'o', color=plotColor)



def toSuperscript(number):
    superscripts = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
        '+': '⁺', '-': '⁻', '=': '⁼', '(': '⁽', ')': '⁾'
    }
    return ''.join(superscripts.get(char, char) for char in str(number))
        
def showFunction(function):
    degree = len(function.coeffArray) - 1
    
    text = ""
    for coeff in function.coeffArray:
        if coeff == 0:  # Skip zero coefficients
            degree -= 1
            continue
        
        if text:
            text += "+" if coeff > 0 else "-"
            
        text += f"{abs(coeff)}"
                
        if degree == 1: text += "x"
        if degree > 1:
            text += f"x{toSuperscript(degree)}"
        
        degree-=1
        
    return text


def findZeros(a, b, c):
    discriminant = b**2-(4*a*c) # discriminant
    
    zeros = np.array([])
    if discriminant < 0:
        print ("This equation has no real solution")
    elif discriminant == 0:
        x = (-b+math.sqrt(discriminant))/(2*a)
        zeros = np.append(zeros, x)
        print ("This equation has one solutions: ", x)
    else:
        x1 = ((-b)+math.sqrt(discriminant))/(2*a)
        x2 = ((-b)-math.sqrt(discriminant))/(2*a)
        zeros = np.append(zeros, [x1,x2])
        print ("This equation has two solutions: ", x1, " and", x2)
    
    return zeros

points = 100
minValues = points*-1
maxValues = points

a = 1
b = -6
c = 11
d = -6
e = 9
f = 12

func = [a,b,c,d,e,f]


func1 = Function(func, min, max)

print(f"Original function: {showFunction(func1)}")
func_derivative = func1.findDerivative()
print(f"The function derivate is {showFunction(func_derivative)}")
#print(f"The function second derivate is {showFunction(func_derivative_second)}")


plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plotFunction(func, True)
plotFunction(func_derivative, False, "f'", "red")
#plotFunction(func_derivative_second, "f''", "yellow")


plt.show()

