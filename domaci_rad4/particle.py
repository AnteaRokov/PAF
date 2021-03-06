import math as ma
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self,v0,kut,m,x0,y0,A,Cx,osnovica = 0,kocka = 0,kugla = 0):   
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
        self.kocka = kocka
        self.kugla = kugla
        self.osnovica = osnovica

    def reset(self):
        del self.osnovica
        del self.kocka
        del self.kugla
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
    
    def plot_kocka_kugla(self):
        if self.kocka == 1:
            self.povrsina = self.osnovica**2
            self.move_Runge_Kutta()
            plt.plot(self.list_x,self.list_y,label ="kocka")
        elif self.kugla == 1:
            d = 2*self.osnovica
            self.povrsina = ((d)**2)*ma.pi/4
            self.move_Runge_Kutta()
            plt.plot(self.list_x,self.list_y,label ="kugla")
        
    def target(self,p,q,r):
        kut = 0
        pogodak = True
        self.kut = (kut/180)* ma.pi
        while pogodak:
            self.move_Runge_Kutta()
            for i in range(len(self.list_x)):
                udaljenost = ((self.list_x[i]-p)**2) + ((self.list_y[i]-q)**2)
                if udaljenost < (r**2): 
                    pogodak = False
            kut = kut + 0.1
            self.kut = (kut/180)* ma.pi
            if kut > 180:
                break
            if pogodak == True:
                self.comeback()
        if kut < 180:    
            return kut

    def plot_target(self,p,q,r):
        kut = self.target(p,q,r)
        if type(kut)==float:
            Circle = plt.Circle((p,q),r, color = "b")
            fig, ax = plt.subplots()
            ax.add_patch(Circle)
            plt.plot(self.list_x,self.list_y,color = "r")
            plt.show()
            return kut