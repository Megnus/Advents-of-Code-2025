# importing library sympy
from sympy import symbols, Eq, solve

# defining symbols used in equations
# or unknown variables
x, y, z = symbols('x,y,z')

# defining equations
eq1 = Eq((x+y+z), 1)
print("Equation 1:")
print(eq1)

eq2 = Eq((x-y+2*z), 1)
print("Equation 2")
print(eq2)

eq3 = Eq((2*x-y+2*z), 1)
print("Equation 3")

# solving the equation and printing the 
# value of unknown variables
print("Values of 3 unknown variable are as follows:")
print(solve((eq1, eq2, eq3), (x, y, z)))

n = 0
a, b, c, d, e, f, g, h = symbols('a,b,c,d,e,f,g,h')
eq1=Eq(n*a+e+f,3)
eq2=Eq(n*a+b+f,5)
eq3=Eq(c+d+e,4)
eq4=Eq(a+b+d,7)
soloution = solve((eq1, eq2, eq3, eq4), (a, b, c, d, e, f))
print(soloution)

result = soloution[a].subs(a, 1)
result = soloution[a].subs({d: 3, f: 2})
print(result)
print('-' * 10)
print('f' in str(soloution.keys()))

for i in soloution.keys():
	print(i)

# a:1, b:3, d:3, e:1, f:2

import numpy as np
#              a  b  c  d  e  f
A = np.array([[0, 0, 0, 0, 1, 1], 
              [0, 1, 0, 0, 0, 1], 
              [0, 0, 1, 1, 1, 0],
              [1, 1, 0, 1, 0, 0],
              ])
y = np.array([3, 5, 4, 7])

x = np.linalg.solve(A, y)
print(x)