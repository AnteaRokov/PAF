import numpy as np
import modul as em
import matplotlib.pyplot as plt

p2 = em.field(0.4,0,0,0,1,np.array([0.1,0.1,0.1]),"0","0","t/10",np.array([0,0,0]))
p2.compare()
p2.cestice()
p2.reset()