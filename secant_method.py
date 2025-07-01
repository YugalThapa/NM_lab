import math 

def f(x):
    # Define your function here
    return math.exp(0.5 * x + 3) + math.cos(0.4 * x) - 50

def secant_method(x0, x1, e = 0.0001, max_iter=100):
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            print("Division by zero encountered. The method fails.")
            return None
        
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        
        print(f"{i+1} -> x0= {round(x0,4)}, x1= {round(x1,4)}, f(x0)= {round(f(x0),4)}, f(x1)= {round(f(x1),4)}, x2= {round(x2,6)}, f(x2)= {round(f(x2),4)}\n")
        
        if abs(f(x2)) <= e:
            print(f"Root found at iteration {i}: {x2}")
            return x2
        
        x0, x1 = x1, x2
    
    print(f"Root not found after {max_iter} iterations.")
    return None

if __name__ == "__main__":
    x0 = int(input("Enter first num:"))  # Initial guess
    x1 = int(input("Enter second num:"))  # Second guess
    secant_method(x0, x1)