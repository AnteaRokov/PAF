from math import sin
from math import cos
from math import pi  
v0 = float(input('Unesite pocetnu brzinu u metrima po sekundi: '))
theta = float(input('Unesite kut otklona u stupnjevima: '))
thetarad = theta*pi/180
g = 9.81

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


    

    








