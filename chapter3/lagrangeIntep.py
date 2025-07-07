import numpy as np

#TAKE INPUT FROM USER
def input_data():
    n = int(input("Enter the number of data points: "))
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(n):
        x[i] = float(input(f"Enter x[{i}]: "))
        y[i] = float(input(f"Enter y[{i}]: "))
    return x, y

#LAGRANGE INTERPOLATION
def lagrange_interpolation(x, y, value):
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (value - x[j]) / (x[i] - x[j])
        result += term
    return result

#MAIN FUNCTION
def main():
    x, y = input_data()
    value = float(input("Enter the value to interpolate: "))
    result = lagrange_interpolation(x, y, value)
    print(f"The interpolated value at x = {value} is: {result}")

#RUN THE MAIN FUNCTION
if __name__ == "__main__":
    main()