#trapezoidal for integration
import math as m

def f(x):
    return m.cos((m.pi*x)/2)+5

def trapezoidal():
    lower_limit = float(input("lower limit: "))
    upper_limit = float(input("upper limit: "))
    interval = int(input("Number of interval: "))

    h = ( upper_limit - lower_limit )/interval

    terms_sum = 0
    for i in range(1,interval):
        terms_sum = terms_sum + f(upper_limit + i*h)

    result = (h/2)*( f(lower_limit) + f(upper_limit) + 2*terms_sum)
    
    print(f"Result = {result} ")

trapezoidal()