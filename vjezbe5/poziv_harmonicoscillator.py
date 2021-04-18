import harmonic_oscillator as harm
import matplotlib.pyplot as plt

h1 = harm.HarmonicOscillator()
h1.init(5, 0.3, 0.2, 5, 0.5)
h1.oscillate(2)
h1.plot_trajectory()
plt.scatter(h1.lista_t_brojac, h1.lista_x, s = 2, c = "red")
h1.reset()


h1 = harm.HarmonicOscillator()
h1.init(5, 0.3, 0.2, 5, 0.5)
h1.analitic(2)
plt.plot(h1.lista_t_brojac, h1.lista_x, c = "green")
h1.reset()

plt.show()





