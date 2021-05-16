import math as ma
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self,v0,kut,m,x0,y0,A,Cx):   
        kut = (kut/180)* ma.pi
        self.v0 = v0
        self.kut = kut
        self.vx = v0*ma.cos(self.kut)
        self.vy = v0*ma.sin(self.kut)
        self.masa = m
        self.x = x0
        self.y = y0
        self.otpor_y = y0
        self.povrsina = A
        self.Cx = Cx
        self.rho = 1.125
        self.dt = 0.01
        self.y0 = y0
        self.x0 = x0
        self.list_x = [x0]
        self.list_y = [y0]

    def reset(self):
        del self.otpor_y
        del self.v0
        del self.x
        del self.y
        del self.kut
        del self.vx
        del self.vy
        del self.masa
        del self.x0
        del self.y0
        del self.povrsina
        del self.Cx
        del self.rho
        del self.dt
        del self.list_x
        del self.list_y

    def comeback(self):
        del self.otpor_y
        del self.vx
        del self.vy
        del self.y
        del self.x
        self.list_x.clear()
        self.list_y.clear()
        self.x = self.x0
        self.y = self.y0
        self.otpor_y = self.y0
        self.list_x.append(self.x)
        self.list_y.append(self.y)
        self.vx = self.v0*ma.cos(self.kut)
        self.vy = self.v0*ma.sin(self.kut)

    def air_resistance_x(self,x):
        if self.kut<ma.pi/2:            #smjer gibanja
            Fx = -((self.vx + x)**2 * self.povrsina * self.Cx* self.rho ) / 2
        else:                                               
            Fx = ((self.vx + x)**2 * self.povrsina * self.Cx* self.rho ) / 2
        return Fx

    def air_resistance_y(self,x):
        if self.otpor_y > self.y:         #smjer gibanja
            Fy = ((self.vy + x)**2 * self.povrsina * self.Cx * self.rho ) / 2   
        else:
            Fy = -((self.vy + x)**2 * self.povrsina * self.Cx * self.rho ) / 2
        return Fy

    def move_euler(self):
        while True:
            if self.y >= 0:
                Akceleracija = self.air_resistance_x(0) / self.masa
                self.vx = self.vx + Akceleracija*self.dt
                self.x = self.x + self.vx * self.dt
                self.list_x.append(self.x)

                Akceleracija_y = self.air_resistance_y(0) / self.masa
                self.vy = self.vy - 9.81*self.dt + Akceleracija_y*self.dt
                self.otpor_y = self.y
                self.y = self.y + self.vy * self.dt
                self.list_y.append(self.y)
            else:
                break

    def move_Runge_Kutta(self):
        while True:
            if self.y >=0:
                k1vx = self.air_resistance_x(0) / self.masa * self.dt
                k1x = self.vx * self.dt
                k2vx = self.air_resistance_x(0.5*k1vx) / self.masa * self.dt
                k2x = (self.vx + 0.5 * k1vx) * self.dt
                k3vx = self.air_resistance_x(0.5*k2vx) / self.masa * self.dt
                k3x = (self.vx + 0.5 * k2vx) * self.dt
                k4vx = self.air_resistance_x(0.5*k3vx) / self.masa * self.dt
                k4x = (self.vx + k3vx) * self.dt
                self.vx = self.vx + (1/6)*(k1vx + 2 * k2vx + 2 * k3vx + k4vx)
                self.x = self.x + (1/6)*(k1x + 2 * k2x + 2 * k3x + k4x)
                self.list_x.append(self.x)
                    
                k1vy = ((self.air_resistance_y(0) / self.masa)-9.81) * self.dt
                k1y = self.vy * self.dt
                k2vy = ((self.air_resistance_y(0.5*k1vy) / self.masa)-9.81) * self.dt
                k2y = (self.vy + 0.5 * k1vy) * self.dt
                k3vy = ((self.air_resistance_y(0.5*k2vy) / self.masa)-9.81) * self.dt
                k3y = (self.vy + 0.5 * k2vy) * self.dt
                k4vy = ((self.air_resistance_y(0.5*k3vy) / self.masa)-9.81) * self.dt
                k4y = (self.vy + k3vy) * self.dt
                self.vy = self.vy + (1/6)*(k1vy + 2 * k2vy + 2 * k3vy + k4vy)
                self.y = self.y + (1/6)*(k1y + 2 * k2y + 2 * k3y + k4y)
                self.list_y.append(self.y)
            else:
                break

    def plot(self):
        plt.plot(self.list_x,self.list_y)
        plt.xlabel('domet x')
        plt.ylabel('domet y')
        plt.show()


    def domet_koeficjent(self):
        self.Cx= 0
        dometi = []
        koeficjenti = []
        for i in range(1000):
            x0 = self.x
            self.move_Runge_Kutta()
            domet = abs(self.list_x[-1] - x0)
            self.comeback()
            dometi.append(domet)
            koeficjenti.append(self.Cx)
            self.Cx += 0.1
        return dometi,koeficjenti

    def domet_masa(self):
        self.masa= 0.1
        dometi = []
        mase = []
        for i in range(1000):
            x0 = self.x
            self.move_Runge_Kutta()
            domet = abs(self.list_x[-1] - x0)
            self.comeback()
            dometi.append(domet)
            mase.append(self.masa)
            self.masa += 0.1
        return dometi,mase

    def plot_domet(self):
        domet,koeficjent = self.domet_koeficjent()
        plt.plot(domet,koeficjent)
        plt.xlabel('domet')
        plt.ylabel('koeficjent')
        plt.show()

        domet,masa = self.domet_masa()
        plt.plot(domet,masa)
        plt.xlabel('domet')
        plt.ylabel('masa')
        plt.show()