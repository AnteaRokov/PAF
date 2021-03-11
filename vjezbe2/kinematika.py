import matplotlib
import matplotlib.pyplot as plt
from math import sin
from math import cos
from math import pi  

def jednoliko_gibanje(F, m, vp, xp):

    a = F/m
    VK = []
    XK = []
    Y = []
    A = []

    for t in range(1,11):
        vk = vp + a*t
        VK.append(vk)

        xk = xp + vk*t
        XK.append(xk)
        Y.append(t)
        A.append(a)
    

    fig1=plt.figure()
    fig1.suptitle('Grafovi')

    plt.subplot(2,2,1)
    plt.plot(Y, XK, label = 'x-t graf')

    plt.subplot(2,2,2)
    plt.plot(Y, VK, label = 'v-t graf')

    plt.subplot(2,2,3)
    plt.plot(Y, A, label = 'a-t graf')
    plt.show()

    
def kosi_hitac(theta, v0, g):
    g = 9.81
    thetarad = theta*pi/180
    X = []
    Y = []
    T = []
    for t in range(1,11):

        sx = (v0*cos(thetarad))*t 
        X.append(sx)

        sy = (v0*sin(thetarad))*t - g * (t/2)
        Y.append(sy)

        T.append(t)
    
    import matplotlib
    import matplotlib.pyplot as plt

    fig1=plt.figure()
    fig1.suptitle('Grafovi')

    plt.subplot(2,2,1)
    plt.plot(X, Y, label = 'x-y graf')

    plt.subplot(2,2,2)
    plt.plot(T, X, label = 'x-t graf')

    plt.subplot(2,2,3)
    plt.plot(T, Y, label = 'y-t graf')
    plt.show()

   




