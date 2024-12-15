def g(x):
    return (6 * x - 5) / x
# Initial guess
x0 = 0.5
iterations = 10
true_root = 1
errors_abs = []

x = x0
for i in range(iterations):

    x_new = g(x)


    absolute_error = abs(x_new - true_root)
    errors_abs.append(absolute_error)

    # Print the current iteration, approximation, and absolute error
    print(f"Iteration {i + 1}: x = {x_new}, Absolute Error = {absolute_error}, true Root = {true_root}")


    x = x_new

print(f"\nFinal approximation after {iterations} iterations: x = {x}")
