import matplotlib.pyplot as plt 
import numpy as np
import math

class gibanje:
    def __init__(self, dt, vrijeme, k, m, v0, x0, func):
        self.vrijeme = vrijeme
        self.func = func
        self.m = m
        self.x0 = x0
        self.v0 = v0
        self.dt = dt
        self.t = []
        self.x = []
        self.a = []
        self.v = []

    def reset(self):
        del self.vrijeme
        del self.func
        del self.m
        del self.x0
        del self.v0
        del self.dt
        del self.t
        del self.x
        del self.a
        del self.v

    def pomak(self):
        dt = self.dt
        v = self.v0
        x = self.x0
        t = 0
        while True:
            sila = self.func(v,x,dt)
            akc = sila / self.m
            v = v + akc*self.dt
            x = x + v*self.dt
            dt = dt + self.dt

            self.t.append(dt)
            self.x.append(x)
            self.a.append(akc)
            self.v.append(v)

            if dt > self.vrijeme:
                break

        
    def graf(self):
        self.pomak()
        plt.plot(self.t , self.x)
        plt.xlabel('vrijeme (s)')
        plt.ylabel('pomak (m)')
        plt.show()

        plt.plot(self.t , self.v)
        plt.xlabel('vrijeme (s)')
        plt.ylabel('brzina (m/s)')
        plt.show()

        plt.plot(self.t , self.a)
        plt.xlabel('vrijeme (s)')
        plt.ylabel('akceleracijia (m/s**2)')
        plt.show()