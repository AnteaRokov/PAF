import derivacija
import math
import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return 5*(x**3) - 2*(x**2) + 2*x -3
def f2(x):
    return math.cos(x)

def derivacija_f1_analiticki(x):
    return  5*3*(x**2) - 2*2*x +2

def derivacija_f2_analiticki(x):
    return -math.sin(x)
   
x, y=derivacija.der_range(f1, 0, 3, 0.1)
plt.scatter(x, y, s = 5)
xs = np.linspace(0, 3, 1000)
plt.plot(xs, 5*3*(xs**2) - 2*2*xs +2, c = 'red')

plt.show()











