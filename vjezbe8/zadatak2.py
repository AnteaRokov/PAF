import Projectile as p
import matplotlib.pyplot as plt

p1 = p.Projectile(8,51,0.14,0,0,0.035,0.1)
p1.move_euler()
plt.plot(p1.list_x,p1.list_y,label = "Eulerova metoda")

p1.comeback()

p1.move_Runge_Kutta()
plt.plot(p1.list_x,p1.list_y,label = "Runge-Kutta")
plt.legend()
plt.show()
p1.reset()