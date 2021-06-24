import zadatak1 as z

p1 = z.Bullet(2, 0) #prvo je h0, pa v0
p1.move_s_otporom_zraka(0.05, 1, 1)
p1.velocity_to_hit_target(50, 1.5, 0.1)
