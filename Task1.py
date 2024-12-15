import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def f(x):
    return x**3 - 2*x**2 - 5

# 1. Plot the graph
x_values = np.linspace(1, 4, 500)
y_values = f(x_values)

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='f(x) = x^3 - 2x^2 - 5', color='blue')
plt.axhline(0, color='red', linestyle='--', label='y = 0')
plt.axvline(0, color='green', linestyle='--', label='x = 0')
plt.grid()
plt.title('Graph of f(x) = x^3 - 2x^2 - 5 (Range: [1, 4])')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()

# 2. Approximate root from the graph
approx_root = 2.6

# 3. Calculate f(x) for the approximate root
approx_f_value = f(approx_root)
print(f"Approximate root from graph: {approx_root}")
print(f"f({approx_root}) = {approx_f_value}")

# 4. Calculate the true root using a numerical method
exact_root = fsolve(f, approx_root)[0]
exact_f_value = f(exact_root)
# Absolute error calculation
absolute_error = abs(exact_root - approx_root)

print(f"Exact root found using fsolve: {exact_root}")
print(f"Absolute error: {absolute_error}")

explanation = """
The graphical root search method is only approximate because it relies on visually estimating where
the graph intersects the x-axis. 
"""
print(explanation)
