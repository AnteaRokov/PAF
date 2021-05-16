import Projectile as p 
import matplotlib.pyplot as plt

p2 = p.Projectile(8,51,0.14,0,0,0.035,0.1)
p2.move_euler()
p2.plot()
p2.reset()


p1 = p.Projectile(8,51,0.14,0,0,0.035,0.1)
p1.move_Runge_Kutta()
p1.plot()
p1.reset()