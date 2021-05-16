import Projectile as p 
import matplotlib.pyplot as plt

p1 = p.Projectile(27,12,0.1,0,0,0.005,0.1,0.11,1,0)
print(p1.plot_target(12,3,1))
p1.reset()

p1 = p.Projectile(27,12,0.1,0,0,0.05,0.1,0.11,1,0)
print(p1.plot_target(0,25,12))
p1.reset()

p1 = p.Projectile(27,12,0.1,0,0,0.05,0.1,0.11,1,0)
print(p1.plot_target(12,22,2))
p1.reset()

p1 = p.Projectile(27,12,0.1,0,0,0.05,0.1,0.11,1,0)
print(p1.plot_target(-12,10,1.2))
p1.reset()