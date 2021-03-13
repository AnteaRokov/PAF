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
    plt.plot(Y, XK)

    plt.subplot(2,2,2)
    plt.plot(Y, VK)

    plt.subplot(2,2,3)
    plt.plot(Y, A)
    plt.show()

    
def kosi_hitac(theta, v0, t):
    a = 9.81
    thetarad = theta*pi/180
    v0x = v0 * cos(thetarad)
    v0y = v0 * sin(thetarad)
    vy = v0y 
    #podjela gibanja nan 100 manjih kako bi se postigla preciznost
    n = 100 
    delta_t = t/n 

    #brojaci
    sx = 0
    sy = 0
    t_brojac = 0 

    #liste gdje se sve pohranjuje 
    X = []
    Y = []
    T = []

    #dodavanje brojaca u listu
    X.append(sx)
    Y.append(sy)
    T.append(t_brojac)

    for i in range(n):

        t_brojac = t_brojac + delta_t
        T.append(t_brojac)

        sx = sx + v0x*delta_t 
        X.append(sx)

        vy = vy - a*delta_t
        sy = sy + vy*delta_t
        Y.append(sy)
        
    

    fig, axes = plt.subplots(2, 2)

    axes[0, 0].plot(X, Y)
    axes[0, 0].set_title('x-y graf')

    axes[0, 1].plot(T, X)
    axes[0, 1].set_title('x-t graf')

    axes[1, 0].plot(T, Y)
    axes[1, 0].set_title('y-t graf')

    plt.show()

   




