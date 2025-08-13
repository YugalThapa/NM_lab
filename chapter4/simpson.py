#simpson method for integration 1/3 rule ( 3 points 2 interval)

import math as m

def f(x):
    return x**2+3

#1/3 rule
def simpson():
    lower_limit = float(input("lower limit: "))
    upper_limit = float(input("upper limit: "))
    interval = int(input("Number of interval: "))
    if (interval <= 0) | (interval % 2 !=0 ):
        print("Interval must be even")

    h = ( upper_limit - lower_limit )/interval

    even_terms_sum = 0
    odd_terms_sum = 0

    for i in range(1,interval):
        if i%2 == 0:
            even_terms_sum = even_terms_sum + f(lower_limit + i*h)
        else:
            odd_terms_sum = odd_terms_sum + f(lower_limit + i*h)

    result = (h/3)*( f(lower_limit) + f(upper_limit) + 4*odd_terms_sum + 2*even_terms_sum)
    
    print(f"result = {result}")

simpson()

#3/8 rule
# def simpson():
#     lower_limit = float(input("lower limit: "))
#     upper_limit = float(input("upper limit: "))
#     interval = int(input("Number of interval: "))
#     if (interval <= 0) | (interval % 2 !=0 ):
#         print("Interval must be even")

#     h = ( upper_limit - lower_limit )/interval

#     three_multiple_sum = 0
#     remaining_terms_sum = 0

#     for i in range(1,interval):
#         if i%3 == 0:
#             three_multiple_sum = three_multiple_sum + f(lower_limit + i*h)
#         else:
#             remaining_terms_sum = remaining_terms_sum + f(lower_limit + i*h)

#     result = (3*h/8)*( f(lower_limit) + f(upper_limit) + 3*remaining_terms_sum + 2*three_multiple_sum)
    
#     print(f"result = {result}")

# simpson()


