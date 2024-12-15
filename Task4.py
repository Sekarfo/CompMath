import cmath

def mullers_method(f, x0, x1, x2, tolerance=1e-6, max_iterations=100):
    for _ in range(max_iterations):

        h0 = x1 - x0
        h1 = x2 - x1
        delta0 = (f(x1) - f(x0)) / h0
        delta1 = (f(x2) - f(x1)) / h1

        D = (2 * (f(x2) - f(x0))) / (h0 + h1)
        E = delta1 - delta0


        discriminant = cmath.sqrt(D ** 2 - 4 * f(x2) * E)


        x3_1 = x2 - (2 * f(x2)) / (D + discriminant)
        x3_2 = x2 - (2 * f(x2)) / (D - discriminant)

        if abs(x3_1 - x2) < abs(x3_2 - x2):
            x2 = x3_1
        else:
            x2 = x3_2

        # Check if the result is within tolerance
        if abs(f(x2)) < tolerance:
            return x2

    return x2

def f(x):
    return x ** 3 + x ** 2 + x + 1

# Initial approximations
x0 = -1
x1 = 0
x2 = 1

# Find the root using Muller's method
root = mullers_method(f, x0, x1, x2)
print(f"Found root: {root}")

# Check the result by substituting the root back into the function
f_value = f(root)
print(f"f(root) = {f_value}")

# Calculate the absolute error
absolute_error = abs(f_value)
print(f"Absolute error: {absolute_error}")
