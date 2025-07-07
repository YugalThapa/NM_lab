import numpy as np
import sys
n = int(input("Enter number of unknowns:"))
a = np.zeros((n,n+1))

x = np.zeros(n)
print("Enter Augmented Matrix Coefficients:")
for i in range(0,n):
  for j in range(n+1):
    a[i][j] = float(input(f"a[{i}][{j}]:"))

# Gauss Elimination method
for i in range(n):
  if a[i][j] == 0.00:
    sys.exit("Divide by zero detected")

  for j in range(i+1,n):
    ratio = a[j][i] / a[i][i]

    for k in range(n+1):
      a[j][k] -= ratio * a[i][k]


x[n-1] = a[n-1][n] / a[n-1][n-1]

for i in range(n-2,-1,-1):
  x[i] = a[i][n]

  for j in range(i+1,n):
    x[i] -= a[i][j] * x[j];

  x[i] /= a[i][j]

print("Require Solution is:",end="\n")
print(x)