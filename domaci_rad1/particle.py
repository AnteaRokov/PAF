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


    def total_time(self):
        ukupno_vrijeme = 0 
        while self.y >= 0:
            self.__move()
            ukupno_vrijeme = ukupno_vrijeme + self.delta_t

        return ukupno_vrijeme


    def max_speed(self):
        while True:
            self.__move()
            if self.y <= 0:
                break
            
        return max(self.V)

    
    def velocity_to_hit_target(self, x_meta, y_meta, r_meta):
        self.v0 = 0
        meta_je_pogodena = False
        self.vx = self.v0 * math.cos(self.thetarad)
        self.vy = self.v0 * math.sin(self.thetarad)

        while True:
            self.__move()

            D = math.sqrt((self.x - x_meta )**2 + (self.y - y_meta )**2)

            if self.y>0:
                
                if D <= r_meta:
                    meta_je_pogodena = True
                    break 
                else:
                    if self.v0 >100:
                        break
            else:
                self.x = 0
                self.y = 0
                self.v0 = self.v0 + 0.3
                self.vx = self.v0 * math.cos(self.thetarad)
                self.vy = self.v0 * math.sin(self.thetarad)
                    

        if meta_je_pogodena:
            print('Brzina iznosi: {}'.format(self.v0))
            return self.v0
        else:
            print('Metu nije moguce pogoditi!')
            

    def angle_to_hit_target(self, x_meta, y_meta, r_meta):
        self.theta = 0
        meta_je_pogodena = False
        self.thetarad = self.theta*math.pi/180
        self.vx = self.v0 * math.cos(self.thetarad)
        self.vy = self.v0 * math.sin(self.thetarad)
        
        while True:
            
            self.__move()

            D = math.sqrt((self.x - x_meta )**2 + (self.y - y_meta )**2)
            if self.y>0:
                if D <= r_meta:
                    meta_je_pogodena = True
                    break 
                else:
                    if self.theta >90:
                        break
            else:
                self.x = 0
                self.y = 0
                self.theta = self.theta + 1
                thetarad = self.theta*math.pi/180
                self.thetarad = thetarad
                self.vx = self.v0 * math.cos(self.thetarad)
                self.vy = self.v0 * math.sin(self.thetarad)

        if meta_je_pogodena:
            print('Kut iznosi: {}'.format(self.theta))
            return self.theta
        else:
            print('Metu nije moguce pogoditi!')
        


        

