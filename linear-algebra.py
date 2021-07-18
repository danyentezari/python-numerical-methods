from sympy import *
x, y, z, t = symbols('x y z t')

M = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(M.det())