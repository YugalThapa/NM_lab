#partial pivoting
# Gauss Elimination Method to solve a system of linear equations

import numpy as np
import sys

n = int (input("Enter the number of rows: "))
a = np.zeros((n, n + 1))
x = np.zeros(n)

#Taking input from user
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input(f"Enter element a[{i}][{j}]: "))

#applying Gauss Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')

    for j in range(0,n):
        if j != i:
            ratio = a[j][i] / a[i][i]
            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

for i in range(n):
    x[i] = a[i][n] / a[i][i]

print(a)
print(x)

