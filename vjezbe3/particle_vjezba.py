import math 
import matplotlib.pyplot as plt
class Particle:
    def init(self, x_0, y_0, v0, theta, delta_t):
        self.x = x_0
        self.y = y_0
        self.v0 = v0
        thetarad = theta*math.pi/180
        self.thetarad = thetarad
        self.delta_t = delta_t 
        self.X = []
        self.Y = []
        self.X.append(x_0)
        self.Y.append(y_0)

        self.vx = self.v0 * math.cos(self.thetarad)
        self.vy = self.v0 * math.sin(self.thetarad) 
        
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

    def __move(self):
        self.vy = self.vy + (-9.81) * self.delta_t

        self.x = self.x + self.vx * self.delta_t
        self.X.append(self.x)

        self.y = self.y + self.vy * self.delta_t
        self.Y.append(self.y)

    
    def range(self):
        while True: 
            self.__move()
            if self.y <= 0:
                break
        
        return max(self.X)
    
    def plot_trajectory(self):
        plt.title('x-y graf')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axis('equal')
        plt.plot(self.X, self.Y)
        plt.show()

    def analiticki_domet(self):
        D = (self.v0**2/9.81) * math.sin(2 * self.thetarad)

        return D
    


   

    
    


         




        

