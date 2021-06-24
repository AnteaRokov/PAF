import zadatak1 as z

p1 = z.Bullet(2, 0) #prvo je h0, pa v0
p1.move(0.01)
p1.velocity_to_hit_target(50, 1.5, 0.1)

p2 = z.Bullet(2, 0)
p2.move(0.05)
p2.velocity_to_hit_target(50, 1.5, 0.1)

p3 = z.Bullet(2, 0)
p3.move(0.1)
p3.velocity_to_hit_target(50, 1.5, 0.1)

