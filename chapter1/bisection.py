import math
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    # Define your function here
    return math.exp(0.5 * x + 3) + math.cos(0.4 * x) - 50

def bisection(a, b, tol=1e-4, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        #print(f"{i+1} -> a= {round(a,4)}, b= {round(b,4)}, f(a)= {round(f(a),4)}, f(b)= {round(f(b),4)}, c= {round(c,6)}, f(c)= {round(f(c),4)}\n")
        if abs(f(c)) < tol:
            print(f"Root found at iteration {i}: {c}")
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print(f"Root not found after {max_iter} iterations. Approximate root: {c}")
    return c


# Plotting the function
x_vals = np.linspace(-10, 10, 400)
y_vals = [f(x) for x in x_vals]

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linewidth=0.8)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x)')
plt.legend()
plt.grid(True)
plt.show()

# Example usage:
root = bisection(1, 2)
print("Approximate root:", root)
