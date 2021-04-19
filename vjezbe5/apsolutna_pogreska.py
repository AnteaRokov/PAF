import harmonic_oscillator as harm 
import matplotlib.pyplot as plt
import numpy as np

h1 = harm.HarmonicOscillator()

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

