import numpy as np
import matplotlib.pyplot as plt

class Function:
    function_coeffs = []
    xpoints = np.array([])
    ypoints = np.array([])
    zerosX = set()
    
    def __init__(self, coeffs, minValues, maxValues):
        self.function_coeffs = coeffs
        self.xpoints = np.arange(minValues, maxValues, 0.05)
        self.preparePlot()
    
    def calcFunction(coeffArray, x):
        result = 0
        degree = len(coeffArray) - 1
        
        for coeff in coeffArray:
            result += coeff * (x ** degree)
            degree -= 1
            
        return result


    def findDerivative(coeffArray):
        degree = len(coeffArray) - 1
        
        derivate = np.array(coeffArray)
        index = 0
        for coeff in coeffArray:
            derivate[index] = coeff * degree
            degree -= 1
            index += 1
            
        derivate = derivate[:-1]
        
        return derivate
            
    def preparePlot(self):
    
        for num in np.sort(self.xpoints):
            newValue = self.calcFunction(self.func, num)
            ypoints = np.append(ypoints, newValue)
            #print(f"x={num}, y={newValue}")
            if round(newValue) == 0: 
                self.zerosX.add(round(num))
            
        
       
