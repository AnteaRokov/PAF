from math import sin
from math import cos
from math import pi  
v0 = float(input('Unesite pocetnu brzinu u metrima po sekundi: '))
theta = float(input('Unesite kut otklona u stupnjevima: '))
thetarad = theta*pi/180
a = 9.81
t = 10
v0x = v0 * cos(thetarad)
v0y = v0 * sin(thetarad)
vy = v0y 

n = 100 
delta_t = t/n 

sx = 0
sy = 0
t_brojac = 0 

X = []
Y = []
T = []

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

import matplotlib
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(X, Y)
axes[0, 0].set_title('x-y graf')

axes[0, 1].plot(T, X)
axes[0, 1].set_title('x-t graf')

axes[1, 0].plot(T, Y)
axes[1, 0].set_title('y-t graf')

plt.show()


    

    








