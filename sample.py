"""
References:
(1) Dany
(2) Gezerlis, 2020, Numerical Methods in Physics with Python.
"""
from math import factorial, log, exp, pi, sin, cos;

# Reference [2, pp. 94]
def f(x):
    return exp(sin(2*x))

def dfdx(x):
    return 2*exp(sin(x))*cos(2*x)

def calc_fd(f,x,h):
    return


# Refernece: [1]
# Cosine implementation with
# Taylor Series
def cos(theta):
    # Using modules because the Period of Cosine is 2\pi
    x = theta % (2*pi)
    term = 0

    # Let k=0, n = 25
    n = 25
    for k in range(0, n):
        numerator = pow(-1, k)*pow(x, 2*k)
        denominator = factorial(2*k)
        term += numerator/denominator
    
    return term

# print(cos(10))


def diff(x, f):
    h = 0.001
    deltax = f(x) + f(x + h)
    deltah = h
    derivative = deltax/deltah
    return derivative


x = 1
f = lambda x: pow(x, 2)


# print(diff(x, f))

print(2**3)

