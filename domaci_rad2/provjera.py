import klass as k 
import matplotlib.pyplot as plt 

def f1(v, x, t):
    return 5 

def f2(v, x, t):
    k = 10
    return -k*x

def f3(v, x, t):
    return (x*t)/v

h1 = k.gibanje(0.1,10, 1, 5, 0, 0, f1)
h1.graf()
h1.reset()

h1 = k.gibanje(0.001,10, 1, 5, 10, 0, f2)
h1.graf()
h1.reset()

h1 = k.gibanje(0.001,10, 1, 5, 10, 3, f3)
h1.graf()
h1.reset()