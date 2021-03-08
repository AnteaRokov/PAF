def  nacrtaj_kruznicu_i_tocku(xi, yi, r, xt, yt):
    x = []
    y = []
    
    for fi in range(1,360):
        rad = fi*pi/180
        xs = xi + r*cos(rad)
        x.append(xs)
        ys = yi + r*sin(rad)
        y.append(ys)
        plt.plot(x, y)
        plt.plot(xs, ys)
    p = input('Zelite li graf ispisati odmah ili u pdf-u? Ako zelite odmah unesite rijec odmah, a ako zelite u pdf-u unesite PDF!')
    if p == 'odmah':
        plt.show()
    elif p == 'PDF':
        ime = input('Unesite ime pod kojim zelite pohraniti svoj pdf: ')
        plt.savefig(f'{ime}.pdf')

import matplotlib
import matplotlib.pyplot as plt
from math import sqrt
from math import pi
from math import cos
from math import sin 
import numpy as np


while True:
    xi = float(input('Unesi x koordinatu ishodišta: '))
    yi = float(input('Unesi y koordinatu ishodišta: '))
    
    if xi == str or yi == str:
        print('Unesene koordinate moraju biti brojevi, a ne stringovi!')
    else:
        break

while True: 
    r = int(input('Unesi radijus kruznice: '))
    
    if r == 0 or r == str:
        print('Radijus kruznice mora biti veci od 0 i ne smije biti string!')
    else:
        break

while True:
    xt = float(input('Unesi x koordinatu tocke: '))
    yt = float(input('Unesi y koordinatu tocke: '))
    
    if xt == str or yt == str:
        print('Unesene koordinate moraju biti brojevi, a ne stringovi!')
    else:
        break
        
d = sqrt((xi - xt)**2 + (yi - yt)**2)

if d > r:
    print('Tocka se nalazi izvan kruznice i udaljena je {} od kruznice!'.format(d-r))
elif d == r:
    print('Tocka se nalazi na kruznicii udaljena je {} od kruznice!'.format(d = r))
else:
    print('Tocka se nalazi unutar kruznice i udaljena je {} od kruznice!'.format(r-d))
        
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')

nacrtaj_kruznicu_i_tocku(xi, yi, r, xt, yt)