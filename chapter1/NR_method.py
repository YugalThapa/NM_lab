import math 

def f(x):
    # Define your function here
    return x**2 - math.sin(x) - 1
 
def g(x):
     return 2*x - math.cos(x)

def newton_raphson(x0, e=0.0001, max_iter=100):
    for i in range(max_iter):
        if g(x0) == 0:
            print("Division by zero encountered. The method fails.")
            return None
        
        x1 = x0 - f(x0) / g(x0)
        #print(f"{i+1} -> x0= {round(x0,4)}, f(x0)= {round(f(x0),4)}, g(x0)= {round(g(x0),4)}, x1= {round(x1,6)}, f(x1)= {round(f(x1),4)}\n")

        if abs(f(x1)) <= e:
            print(f"Root found at iteration {i}: {x1}")
            return x1
        
        x0 = x1
        
    print(f"Root not found after {max_iter} iterations. ")
    return None


if __name__ == "__main__":
    x0 = float(input("Enter initial guess: "))  # Initial guess
    newton_raphson(x0)