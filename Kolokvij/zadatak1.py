import math 
import matplotlib.pyplot as plt
class VertikalniHitac:
    def __init__(self, h, v):
        self.h = h
        self.v = v
        
    def ispis_podataka(self):
        print('Objekt je stvoren.', 'Visina iznosi: ', self.h, 'Brzina iznosi: ', self.v)


p1 = VertikalniHitac(3, 5)
p1.ispis_podataka()

    