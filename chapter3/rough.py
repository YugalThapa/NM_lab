# Runge-Kutta 4th Order Method for first-order ODE
# Solves dy/dx = f(x, y) from x0 to xn with step size h

def f(x, y):
    """Define the differential equation dy/dx = f(x, y)."""
    return x * y  # Example: dy/dx = x*y

def runge_kutta4(x0, y0, xn, h):
    """Runge-Kutta 4th order method."""
    n = int((xn - x0) / h)  # number of steps
    
    x = x0
    y = y0
    
    print(f"{'x':>10} {'y':>10}")
    print(f"{x:10.5f} {y:10.5f}")
    
    for i in range(1, n + 1):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
        
        print(f"{x:10.5f} {y:10.5f}")

# Example usage
x0 = 0
y0 = 1
xn = 2
h = 0.5

runge_kutta4(x0, y0, xn, h)
