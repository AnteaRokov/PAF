import math 
import matplotlib.pyplot as plt
class VertikalniHitac:
    def init(self, x_0, y_0, v0, theta, delta_t):
        self.x = x_0
        self.y = y_0  #ovo mi je visina
        self.v0 = v0
        thetarad = theta*math.pi/180
        self.thetarad = thetarad
        self.delta_t = delta_t 
        self.t_brojac = 0
        self.lista_t_brojac = []
        self.lista_t_brojac.append(self.t_brojac)
        self.X = []
        self.Y = []
        self.X.append(x_0)
        self.Y.append(y_0)

        self.vx = self.v0 * math.cos(self.thetarad)
        self.vy = self.v0 * math.sin(self.thetarad)
        self.V = [] 
    
        
    def reset(self):
        self.x = 0 
        self.y = 0
        self.v0 = 0 
        self.thetarad = 0
        self.delta_t = 0
        self.X = []
        self.Y = []
        self.vx = 0 
        self.vy = 0
        self.V = []

    def __move(self):
        self.vy = self.vy + (-9.81) * self.delta_t

        self.x = self.x + self.vx * self.delta_t
        self.X.append(self.x)

        self.y = self.y + self.vy * self.delta_t
        self.Y.append(self.y)

        self.v = math.sqrt(self.vx**2 + self.vy**2)
        self.V.append(self.v)

        self.t_brojac = self.t_brojac + self.delta_t
        self.lista_t_brojac.append(self.t_brojac)

    def gibanje(self):
    
        while self.y >= 0:
            self.__move()
  
        return self.Y, self.lista_t_brojac
        
    
    def plot_trajectory(self):
        plt.title('h-t graf')
        plt.xlabel('t')
        plt.ylabel('h')
        plt.axis('equal')
        plt.plot(self.lista_t_brojac, self.Y)
        plt.show()


    def gibanje_2(self):
        while self.y >= 0:
            self.__move()
  
        return self.X, self.lista_t_brojac

    def plot_trajectory_2(self):
        plt.title('v-t graf')
        plt.xlabel('t')
        plt.ylabel('v')
        plt.axis('equal')
        plt.plot(self.lista_t_brojac, self.X)
        plt.show()

