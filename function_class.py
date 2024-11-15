import math
import numpy as np
import matplotlib.pyplot as plt

def toSuperscript(number):
    superscripts = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
        '+': '⁺', '-': '⁻', '=': '⁼', '(': '⁽', ')': '⁾'
    }
    return ''.join(superscripts.get(char, char) for char in str(number))


class Function:
    coefficients = []
    points = 0
    minValues = 0
    maxValues = 0
    xpoints = np.array([])
    ypoints = np.array([])
    zerosX = set()
    
    def __init__(self, coeffs, points):
        self.coefficients = coeffs
        self.points = points
        self.minValues = points*-1
        self.maxValues = points
        self.xpoints = np.arange(self.minValues, self.maxValues, 0.05)
        self.preparePlot()
    
    def calcFunction(self, x):
        result = 0
        degree = len(self.coefficients) - 1
        
        for coeff in self.coefficients:
            result += coeff * (x ** degree)
            degree -= 1
            
        return result

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

    def findDerivative(self):
        degree = len(self.coefficients) - 1
        
        derivate = np.array(self.coefficients)
        index = 0
        for coeff in self.coefficients:
            derivate[index] = coeff * degree
            degree -= 1
            index += 1
            
        derivate = derivate[:-1]
        
        return derivate
            
    def preparePlot(self):
    
        for num in np.sort(self.xpoints):
            newValue = self.calcFunction(num)
            self.ypoints = np.append(self.ypoints, newValue)
            #print(f"x={num}, y={newValue}")
            if round(newValue) == 0: 
                self.zerosX.add(round(num))
            
    def plotFunction(self, showZeros, func_name_label = "f", plotColor = "blue"):
    
        plt.plot(self.xpoints, self.ypoints, color=plotColor, label=f"{func_name_label}(x)={self.showFunction()}")
        plt.legend(fontsize=14)
        
        if showZeros:
            print(f"The zeroes of the function are: {self.zerosX}")
            zerosY = np.array(np.zeros(len(self.zerosX)))
            
            plt.plot(list(self.zerosX), zerosY, 'o', color=plotColor)



            
    def showFunction(self):
        degree = len(self.coefficients) - 1
        
        text = ""
        for coeff in self.coefficients:
            if coeff == 0:  # Skip zero coefficients
                degree -= 1
                continue
            
            if text:
                text += "+" if coeff > 0 else "-"
            else:
                text += "-" if coeff < 0 and not text else ""
                
            text += f"{abs(coeff)}"
                    
            if degree == 1: text += "x"
            if degree > 1:
                text += f"x{toSuperscript(degree)}"
            
            degree-=1
            
        return text
        
       
