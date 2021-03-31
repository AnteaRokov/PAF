import particle_vjezba as prt 
p1 = prt.Particle()
p1.init(0, 0, 10, 30, 0.01)
print(p1.range())
p1.plot_trajectory()
p1.reset()
