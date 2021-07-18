from sympy import *
x,y,z = symbols('x y z')


fu = x**2+y**3

# Second-order partial derivative
print(diff(fu, y, 2))


chi_sq = 3