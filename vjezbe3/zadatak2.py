import particle_vjezba as prt 
import matplotlib.pyplot as plt

p1 = prt.Particle()
DT = []
dt = 0.000
GRESKA = []

for i in range(100):
    dt = dt + 0.001
    p1.init(0, 0, 10, 30, dt)
    greska = abs(p1.range() - p1.analiticki_domet())/p1.analiticki_domet()*100
    DT.append(dt)
    GRESKA.append(greska)
    p1.reset()

plt.xlabel('dt/s')
plt.ylabel('greska/ % ')
plt.plot(DT, GRESKA)
plt.show()
