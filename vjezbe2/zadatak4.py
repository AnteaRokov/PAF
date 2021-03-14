from math import sin, cos
from math import pi
from math import sqrt
import matplotlib
import matplotlib.pyplot as plt
g = 9.81

def kraj_gibanja(v0, g, theta, pi, t_maks):

    thetarad = theta*pi/180
      
    v0x = v0 * cos(thetarad)
    v0y = v0 * sin(thetarad)
    vy = v0y

    n = 100 
    delta_t = t_maks/n 

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

        vy = vy - g*delta_t
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




def maks_visina(v0, g, pi, theta):
    thetarad = theta*pi/180
    ymaks = (v0**2)/(2*g) * (sin(thetarad))**2
    return print('Najveca visina iznosi: {}'.format(ymaks))




def domet(v0, g, pi, theta):
    thetarad = theta*pi/180
    D = (v0**2/g)*sin(thetarad)
    return print('Domet iznosi: {}'.format(D))


def maks_brzina(v0, theta, pi, g):
    thetarad = theta*pi/180
    t_maks = (2*v0*sin(thetarad))/g
    v0x = v0 * cos(thetarad)
    vx = v0x*cos(thetarad)
    vy = v0*sin(thetarad)-g*t_maks
    v_maks = sqrt((vx)**2 + (vy)**2)
    return print('Maksimalna brzina  iznosi: {}'.format(v_maks))
    


def meta_i_hitac(v0, theta,pi, t_maks, sy0):

    thetarad = theta*pi/180
    xm = float(input('Unesi x koordinatu mete: '))
    ym = float(input('Unesi y koordinatu mete: '))
    r = int(input('Unesi radijus mete: '))
    
    v0x = v0 * cos(thetarad)
    v0y = v0 * sin(thetarad)
    vy = v0y

    a = 9.81

    n = 1000 
    t = 10
    delta_t = t_maks/n 

    sx = 0
    sy = sy0

    X = []
    Y = []

    X.append(sx)
    Y.append(sy)

    minimalna_udaljenost = sqrt((xm)**2 + (ym - sy0)**2)
    
    i = False 

    while True:

        sx = sx + v0x*delta_t 
        vy = vy - g*delta_t
        sy = sy + vy*delta_t

        if sy <= 0:
            break 

        X.append(sx)
        Y.append(sy)
        udaljenost = sqrt((xm)**2 + (ym - sy0)**2)

        if udaljenost <= r:
            i = True
            break

        else:
            if udaljenost - r < minimalna_udaljenost:
                minimalna_udaljenost = udaljenost - r
        
    if i:
        print('Meta je pogodena.')

    else:
        print('Meta nije pogodena. Najmanja udaljenost iznos: {}'.format(minimalna_udaljenost))
    
    x_graf = []
    y_graf = []

    for pi in range(1, 3600):
        apcisa = xm + r*cos(pi/10)
        ordinata = ym + r*sin(pi/10)
        x_graf.append(apcisa)
        y_graf.append(ordinata)
    
    plt.plot(x_graf, y_graf)
    plt.plot(X, Y)
    plt.show()



        




