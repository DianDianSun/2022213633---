import numpy as np
x = np.linspace(0,1,100000)
y = np.exp(x)
dx = x[1]-x[0]
S = np.sum(y*dx)
exact = np.e - 1
error = np.abs(exact - S)
print("估算值:",S)
print("精确值:",exact)
print("误差:",error)