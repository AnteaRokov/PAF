import numpy as np 
import matplotlib.pyplot as plt

def three_step(f, x, h):
    return (f(x+h) - f(x-h)) / (2*h)

def two_step(f, x, h):
    return (f(x+h) - f(x)) / h

def der_range(f, a, b, h, izbor = 0):
    x_list = []
    fx_list = []

    if izbor == 1:
        for x in np.arange(a, b, h):
            x_list.append(x)
            fx_list.append(three_step(f, x, h))
    else:
        for x in np.arange(a, b, h):
            x_list.append(x)
            fx_list.append(two_step(f, x, h))

    return x_list, fx_list

def integrate_rectangle(f ,a ,b ,n):
    delta_x = (b-a)/n 
    gornja_meda = 0
    donja_meda = 0
    gornja = a + delta_x    
    donja = a    
    for i in range(n):
        gornja_meda = gornja_meda + f(gornja) * delta_x
        gornja = gornja + delta_x
        donja_meda = donja_meda + f(donja) * delta_x
        donja = donja + delta_x
    
    return gornja_meda, donja_meda
    
def integrate_trapeze(f, a, b, n):
    delta_x = (b-a)/n
    suma = 0
    x = a
    for i in range(n):
        suma = suma + f(x)
        x = x + delta_x
    integral = suma*delta_x + ((f(b) + f(a))/2)*delta_x
    
    return integral
    







