#linear regression 

import numpy as np

def take_input():
    n = int(input("Enter the number of data points: "))
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(n):
        x[i] = float(input(f"Enter x[{i}]: "))
        y[i] = float(input(f"Enter y[{i}]: "))
    return x, y

def regression(x, y, val):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_xy = np.sum(x * y)

    # Calculate slope (m) and intercept (b)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    c = (sum_y - m * sum_x) / n

    print(f"Linear Regression Equation: y = {m:.2f}x + {c:.2f}")

    return val * m + c

x,y = take_input()
val = float(input("calculate regression for: "))
print(regression(x, y, val))
