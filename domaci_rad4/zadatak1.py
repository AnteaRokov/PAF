import Projectile as p 
import matplotlib.pyplot as plt

p1 = p.Projectile(8,51,0.14,0,0,0.035,0.1,0.11,1,0)
p1.plot_kocka_kugla()

p2 = p.Projectile(8,51,0.14,0,0,0.035,0.1,0.11,0,1)
p2.plot_kocka_kugla()

plt.legend()
plt.show()
p1.reset()
p2.reset()