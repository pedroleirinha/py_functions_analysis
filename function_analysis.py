import matplotlib.pyplot as plt
from function_class import Function

# coeff = [1, 5, -10]
# print(f"roots: {np.polynomial.polynomial.polyroots(coeff)}")
points = 100

a = 1
b = -6
c = 11
d = -6

function_values = [a,b,c,d]

func1 = Function(function_values)
func_derivative = Function(func1.findDerivative())
func_derivative_second = Function(func_derivative.findDerivative())

print(f"Original function: {func1.showFunction()}")
print(f"The function derivate is {func_derivative.showFunction()}")
#print(f"The function second derivate is {showFunction(func_derivative_second)}")

plt.xlim(-10, 20)
plt.ylim(-20, 30)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

func1.plotFunction(True)
func_derivative.plotFunction(False, "f'", "red")
#plotFunction(func_derivative_second, False, "f''", "yellow")

plt.show()