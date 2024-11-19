import matplotlib.pyplot as plt
from function_class import Function

points = 10

a = 2
b = -3
c = -5
d = -6
e = 0
f = 0

function_values = [a,b,c,d]

func1 = Function(function_values, points)
func_derivative = Function(func1.findDerivative(), points)
#func_derivative_second = Function(func_derivative.findDerivative(), points)

print(f"Original function: {func1.showFunction()}")
print(f"The function derivate is {func_derivative.showFunction()}")
#print(f"The function second derivate is {showFunction(func_derivative_second)}")

plt.xlim(-10, 20)
plt.ylim(-20, 30)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

#print(f"roots: {np.polynomial.polynomial.polyroots(function_values)}")
func1.plotFunction(True)
func_derivative.plotFunction(False, "f'", "red")
#plotFunction(func_derivative_second, False, "f''", "yellow")

plt.show()