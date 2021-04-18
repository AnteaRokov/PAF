import matplotlib.pyplot as plt
import math
class HarmonicOscillator:
    def init(self, v, A, k, m, delta_t):

        self.v = v
        self.a = (-k/m) * A
        self.x = A 
        self.k = k
        self.m = m 

        self.delta_t = delta_t 
        self.t_brojac = 0

        self.lista_delta_t = []
        self.lista_v = []
        self.lista_x = []
        self.lista_a = []
        self.lista_t_brojac = []
        
        self.lista_v.append(self.v)
        self.lista_x.append(self.x)
        self.lista_a.append(self.a)
        self.lista_t_brojac.append(self.t_brojac)

    def reset(self):
        del self.m
        del self.k
        del self.a
        del self.v
        del self.x
        del self.delta_t
        del self.t_brojac
        del self.lista_delta_t
        del self.lista_v 
        del self.lista_x 
        del self.lista_a 
        del self.lista_t_brojac 


    def __move(self):

        self.v = self.v + self.a * self.delta_t
        self.x = self.x + self.v * self.delta_t
        self.a = (-self.k / self.m) * self.x 
        self.t_brojac = self.t_brojac + self.delta_t

        self.lista_v.append(self.v)
        self.lista_x.append(self.x)
        self.lista_a.append(self.a)
        self.lista_t_brojac.append(self.t_brojac)

    def oscillate(self, t):
        while self.t_brojac <= t:
            self.__move()
  
        return self.lista_x, self.lista_t_brojac
        

    def plot_trajectory(self):
        plt.figure('Harmonic oscillator')

        plt.subplot(2, 2, 1)
        plt.plot(self.lista_t_brojac, self.lista_x)
        plt.title('x-t graf')
        plt.xlabel('t / s')
        plt.ylabel('x / m')
        
        plt.subplot(2, 2, 2)
        plt.plot(self.lista_t_brojac, self.lista_v)
        plt.title('v-t graf')
        plt.xlabel('t / s')
        plt.ylabel('v / (m/s)')

        plt.subplot(2, 2, 3)
        plt.plot(self.lista_t_brojac, self.lista_a)
        plt.title('a-t graf')
        plt.xlabel('t / s')
        plt.ylabel('a / (m/s^2)')

        plt.subplots_adjust(wspace = 0.5, hspace = 0.7)

        plt.show()

    def analitic(self, t):                  #analiticki izracun putanje
        self.lista_x = []
        self.lista_t_brojac = []
        self.alfa = math.sqrt(self.k/self.m)
        self.fi = math.pi/2
        self.t_brojac = 0

        while self.t_brojac <= t:
            x = self.x * math.sin(self.alfa*self.t_brojac + self.fi)
            self.t_brojac = self.t_brojac + self.delta_t
            self.lista_x.append(x)
            self.lista_t_brojac.append(self.t_brojac)
            
        return self.lista_x, self.lista_t_brojac

    def period(self):
        T = 0
        while True:
            self.__move()
            if self.x < 0:
                T = 0
                break
        while True:
            self.__move()
            T = T + self.delta_t
            if self.x > 0:
                break
        return 2*T


    def period_analiticki(self):
        return 2*math.pi*math.sqrt(self.m/self.k)
    
    


            
        

        



        





        
            
            



