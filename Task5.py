import matplotlib.pyplot as plt


def false_position_method(f, x0, x1, tolerance=1e-6, max_iterations=100):
    errors_abs = []
    for iteration in range(max_iterations):

        denominator = f(x1) - f(x0)

        if denominator == 0:
            print("Denominator is zero. Function values at x0 and x1 are the same.")
            return None, errors_abs

        x2 = x1 - (f(x1) * (x1 - x0)) / denominator

        absolute_error = abs(f(x2))
        errors_abs.append(absolute_error)

        relative_error = abs(x2 - x1) / abs(x2)

        print(f"Iteration {iteration + 1}:")
        print(f"x2 = {x2}, Absolute Error = {absolute_error}, Relative Error = {relative_error}")


        if absolute_error < tolerance:
            return x2, errors_abs

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
    return x2, errors_abs



def f(x):
    return x ** 2 - 2 * x


x0 = 1
x1 = 15


root, errors_abs = false_position_method(f, x0, x1)

if root is not None:

    print(f"\nRoot: {root}")


    plt.plot(errors_abs, label="Absolute Error")
    plt.xlabel('Iteration')
    plt.ylabel('Absolute Error')
    plt.title('Absolute Error vs Iteration for False Position Method')
    plt.grid(True)
    plt.show()
