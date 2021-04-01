import matplotlib.pyplot as plt
import math
import particle as prt

def ovisnost_dometa_o_kutu_otklona():
    theta_lista = []
    theta = 0
    theta_lista.append(theta)

    domet_lista = []
    domet = 0 
    domet_lista.append(domet)

    p1 = prt.Particle()

    for theta in range(90):
        p1.init(0, 0, 30, theta, 0.01)
        domet = p1.range()
        theta_lista.append(theta)
        domet_lista.append(domet)
        p1.reset()
    
    plt.plot(theta_lista, domet_lista)
    plt.title('Ovisnost dometa o pocetnom kutu otklona')
    plt.xlabel('Kut otklona / °')
    plt.ylabel('Domet / m')
    plt.show()


def ovisnost_vremena_o_kutu_otklona():
    theta = 0
    theta_lista = []
    theta_lista.append(theta)

    t = 0 
    t_lista = []
    t_lista.append(t)

    p1 = prt.Particle()

    for theta in range(90):
        p1.init(0, 0, 30, theta, 0.01)
        t = p1.total_time()
        theta_lista.append(theta)
        t_lista.append(t)
        p1.reset()

    plt.plot(theta_lista, t_lista)
    plt.title('Ovisnost vremena o početnom kutu otklona')
    plt.xlabel('Kut otklona / °')
    plt.ylabel('Vrijeme / s')
    plt.show()


ovisnost_dometa_o_kutu_otklona()
ovisnost_vremena_o_kutu_otklona()




