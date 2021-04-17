import matplotlib.pyplot as plt
import math
import derivacija 

def f1(x):
    return 2*x*x - 3

def integrirano_f1(x):
    return (2/3)*x**3 - 3*x

a = 0
b = 10
delta_n = 500
n_lista = []
sve_gornje_mede = []
sve_donje_mede = []
analiticko = []
trapez = []

for i in range(1, 40):
    n_lista.append(delta_n*i)

for n in n_lista:
    gor, donj = derivacija.integrate_rectangle(f1,a,b,n)
    sve_gornje_mede.append(gor)
    sve_donje_mede.append(donj)
    integral_trapeze = derivacija.integrate_trapeze(f1 ,a ,b ,n)
    trapez.append(integral_trapeze)
    integral_analiticki = integrirano_f1(b) - integrirano_f1(a)
    analiticko.append(integral_analiticki)

plt.scatter(n_lista, sve_gornje_mede, s = 2, c = "red")
plt.scatter(n_lista, sve_donje_mede, s = 2, c = "orange")
plt.scatter(n_lista, trapez, s = 2, c = "green")
plt.plot(n_lista, analiticko)
plt.show()
