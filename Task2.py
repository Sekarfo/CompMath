import numpy as np
from scipy.optimize import fsolve

# Define the function
def f(x):
    return np.exp(x) - 2*x - 3

# 1. Bisection Method
def bisection_method(func, a, b, tol=1e-6):
    iterations = 0
    while (b - a) / 2 > tol:
        iterations += 1
        midpoint = (a + b) / 2
        if func(midpoint) == 0:
            return midpoint, iterations
        elif func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2, iterations

# 2. Secant Method
def secant_method(func, x0, x1, tol=1e-6):
    iterations = 0
    while abs(x1 - x0) > tol:
        iterations += 1
        f_x0 = func(x0)
        f_x1 = func(x1)
        if f_x1 - f_x0 == 0:
            return None, iterations
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x2
    return x1, iterations

# 3. Exact Root
exact_root = fsolve(f, 1)[0]
exact_f_value = f(exact_root)

bisection_root, bisection_iterations = bisection_method(f, 0, 2)
secant_root, secant_iterations = secant_method(f, 0, 2)

# Calculate relative errors
bisection_error = abs(bisection_root - exact_root) / abs(exact_root)
secant_error = abs(secant_root - exact_root) / abs(exact_root)


print(f"Exact root (fsolve): {exact_root:.6f}")
print(f"Bisection Method: Root = {bisection_root:.6f}, Iterations = {bisection_iterations}, Relative Error = {bisection_error:.3e}")
print(f"Secant Method: Root = {secant_root:.6f}, Iterations = {secant_iterations}, Relative Error = {secant_error:.3e}")
