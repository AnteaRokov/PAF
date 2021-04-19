import math 
import matplotlib.pyplot as plt
class VertikalniHitac:
    def init(self, h, v):
        self.h = h
        self.v = v
        
    def ispis_podataka(self):
        print('Objekt je stvoren.', 'Visina iznosi: ', self.h, 'Brzina iznosi: ', self.v)

    def reset_visina(self):
        del self.h
    
    def reset_brzina(self):
        del self.v


