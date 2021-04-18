import harmonic_oscillator as harm 
import matplotlib.pyplot as plt
import numpy as np

h1 = harm.HarmonicOscillator()


def preciznost():
    lista_delta_t = list(np.linspace(0.01,0.11, 50))
    lista_numericki_period = []
    analiticki_period = []

    for delta_t in lista_delta_t:
        h1.init(0.1 ,2 , 0, 0.1, delta_t)    
        lista_numericki_period.append(h1.period())
        analiticki_period.append(h1.period_analiticki())
        h1.reset()

    plt.plot(lista_delta_t, analiticki_period)
    plt.scatter(lista_delta_t, lista_numericki_period, s = 3, c = "blue")
    plt.show()


def apsolutna_pogreska():
    lista_delta_t = list(np.linspace(0.01 ,0.11 , 50))
    apsolutna_pogreska = []

    for delta_t in lista_delta_t:
        h1.init(0.1 ,2 ,0 ,0.1 ,delta_t)  
        greska = (abs(h1.period() - h1.period_analiticki()) / h1.period_analiticki()) * 100
        apsolutna_pogreska.append(greska)

    plt.plot(lista_delta_t, apsolutna_pogreska)
    plt.show()

apsolutna_pogreska()
preciznost()
