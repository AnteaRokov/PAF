import particle as prt

p1 =prt.Particle(10, -5) 
p1.printInfo()

p2 = prt.Particle(12, 3)
p2.printInfo()
p2.mass = 7
p2.printInfo()

p1.udaljenost_od_ishodista()
p1.udaljenost_od_tocke()
