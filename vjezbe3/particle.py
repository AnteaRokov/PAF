import math 
class Particle:
    def __init__(self, mass, x_0):
        self.mass = mass
        self.x_0 = x_0

    def printInfo(self):
        print('Cestica ima masu {} i u pocetnom trenutku nalazi se na polozaju X = {}'.format(self.mass, self.x_0))
    
    def udaljenost_od_ishodista(self):
        print('Udaljenost od ishodista iznosi: {}'.format(abs(self.x_0 - 0)))
    
    def udaljenost_od_tocke(self):
        x = float(input('Unesi x koordinatu tocke: '))
        self.x = x
        print('Udaljenost izmedu tocaka iznosi: {}'.format(abs(self.x - self.x_0)))