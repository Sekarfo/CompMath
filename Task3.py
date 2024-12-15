import matplotlib.pyplot as plt

def newton_raphson_method(func, derivative, x0, tol=1e-6, max_iter=100):
    iterations = []
    abs_errors = []


    for i in range(max_iter):
        f_x0 = func(x0)
        df_x0 = derivative(x0)
        if df_x0 == 0:
            break

        x1 = x0 - f_x0 / df_x0
        abs_error = abs(x1 - x0)
        rel_error = abs_error / abs(x1) if x1 != 0 else 0

        iterations.append((i + 1, x0, abs_error, rel_error))
        abs_errors.append(abs_error)

        if abs_error < tol:
            break

        x0 = x1

    return x1, iterations, abs_errors

def func(x):
    return x**2 - 3*x + 2

def derivative(x):
    return 2*x - 3

x0 = 2.5
root, iteration_data, abs_errors = newton_raphson_method(func, derivative, x0)

print("Iteration | Current Guess | Absolute Error | Relative Error")
for iter_num, guess, abs_err, rel_err in iteration_data:
    print(f"{iter_num:9d} | {guess:13.6f} | {abs_err:14.6f} | {rel_err:13.6f}")

# Plot convergence graph
plt.plot(range(1, len(abs_errors) + 1), abs_errors, marker='o', linestyle='-', color='b')
plt.xlabel('Iteration Number')
plt.ylabel('Absolute Error')
plt.title('Convergence of Newton-Raphson Method')
plt.grid()
plt.show()

