import particle as prt 
p1 = prt.Particle()
p1.init(0, 0, 10, 30, 0.01)
print(p1.total_time())
print(p1.max_speed())
print(p1.velocity_to_hit_target(1, 2, 1))
print(p1.angle_to_hit_target(1, 2, 1))
