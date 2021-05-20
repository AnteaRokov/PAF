import matplotlib.pyplot as plt

class BungeeJumping: 
    def __init__(self, y0, l0, k, m, ro = 1, Cd = 1, A = 1, AirResistance = False):
        self.y0 = y0
        self.l0 = l0
        self.k = k
        self.m = m 
        self.ro = ro 
        self.Cd = Cd
        self.A = A 
        self.AirResistance = AirResistance
        self.y = y0
        self.v = 0 
        self.t = 0 
        self.lista_y = []
        self.lista_t = []

        self.lista_y.append(self.y0)
        self.lista_t.append(self.t)

        self.Ep = self.m * 9.81 * self.y
        self.Ek = 0 
        self.Ee = 0
        self.E = self.Ep + self.Ek + self.Ee

        self.lista_Ep = []
        self.lista_Ek = []
        self.lista_Ee = []
        self.lista_E = []

        self.lista_Ep.append(self.Ep)
        self.lista_Ek.append(self.Ek)
        self.lista_Ee.append(self.Ee)
        self.lista_E.append(self.E)


    def reset(self):
        del self.y0
        del self.l0
        del self.k
        del self.m
        del self.ro
        del self.Cd
        del self.A
        del self.AirResistance
        del self.y
        del self.v
        del self.t
        del self.lista_y
        del self.lista_t
        del self.Ep
        del self.Ek
        del self.Ee
        del self.E
        del self.lista_Ep
        del self.lista_Ek
        del self.lista_Ee
        del self.lista_E


    def povratak_na_pocetak(self):
        y0 = self.y0
        l0 = self.l0
        k = self.k
        m = self.m
        ro = self.ro
        Cd = self.Cd
        A = self.A
        AirResistance = self.AirResistance
        self.reset()

        self.y0 = y0
        self.l0 = l0
        self.k = k
        self.m = m
        self.ro = ro
        self.Cd = Cd
        self.A = A
        self.AirResistance = AirResistance
        self.y = y0
        self.v = 0
        self.t = 0
        self.lista_y = []
        self.lista_t = []
        self.lista_y.append(self.y)
        self.lista_t.append(self.t)
        self.Ep = m * 9.81 * self.y
        self.Ek = 0
        self.Ee = 0
        self.E = self.Ep + self.Ek + self.Ee
        self.lista_Ep = []
        self.lista_Ek = []
        self.lista_Ee = []
        self.lista_E = []
        self.lista_Ep.append(self.Ep)
        self.lista_Ek.append(self.Ek)
        self.lista_Ee.append(self.Ee)
        self.lista_E.append(self.E)


    def elasticna_sila(self):
        razlika = self.y0 - self.y - self.l0
        if razlika > 0:
            F = self.k * razlika
        else:
            F = 0
        return F

    def otpor_zraka(self):
        F = - abs(self.v) * self.v * self.ro * self.Cd * self.A * 0.5
        return F

    def elasticna_energija(self):
        razlika = self.y0 - self.y - self.l0
        if razlika > 0:
            E = 0.5 * self.k * razlika * razlika
        else:
            E = 0
        return E
    
    def __pokreni(self, delta_t):
        a = -9.81 + self.elasticna_sila()/self.m
        self.v = self.v + a * delta_t
        self.y = self.y + self.v * delta_t
        self.t = self.t + delta_t
        self.Ep = self.m * 9.81 * self.y
        self.Ek = 0.5 * self.m * self.v * self.v
        self.Ee = self.elasticna_energija()
        self.E = self.Ep + self.Ek + self.Ee

        self.lista_y.append(self.y)
        self.lista_t.append(self.t)
        self.lista_Ep.append(self.Ep)
        self.lista_Ek.append(self.Ek)
        self.lista_Ee.append(self.Ee)
        self.lista_E.append(self.E)

    
    def __pokreni_sa_otporom_zraka(self, delta_t):
        a = -9.81 + (self.elasticna_sila() + self.otpor_zraka())/self.m
        self.v = self.v + a * delta_t
        self.y = self.y + self.v * delta_t
        self.t = self.t + delta_t
        self.Ep = self.m * 9.81 * self.y
        self.Ek = 0.5 * self.m * self.v * self.v
        self.Ee = self.elasticna_energija()
        self.E = self.Ep + self.Ek + self.Ee
        self.lista_y.append(self.y)
        self.lista_t.append(self.t)
        self.lista_Ep.append(self.Ep)
        self.lista_Ek.append(self.Ek)
        self.lista_Ee.append(self.Ee)
        self.lista_E.append(self.E)


    def pokreni_2(self ,T ,delta_t):
        if self.AirResistance:
            while self.t < T:
                self.__pokreni_sa_otporom_zraka(delta_t)
        else:
            while self.t < T:
                self.__pokreni(delta_t)


p1 = BungeeJumping(100,50,500,50)
p1.pokreni_2(50,0.001)
p2 = BungeeJumping(100,50,500,50,1.22,2,0.1,True)
p2.pokreni_2(50,0.001)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(p1.lista_t, p1.lista_y)
axs[0, 1].plot(p1.lista_t, p1.lista_Ep)
axs[0, 1].plot(p1.lista_t, p1.lista_Ek)
axs[0, 1].plot(p1.lista_t, p1.lista_Ee)
axs[0, 1].plot(p1.lista_t, p1.lista_E)
axs[1, 0].plot(p2.lista_t, p2.lista_y)
axs[1, 1].plot(p2.lista_t, p2.lista_Ep)
axs[1, 1].plot(p2.lista_t, p2.lista_Ek)
axs[1, 1].plot(p2.lista_t, p2.lista_Ee)
axs[1, 1].plot(p2.lista_t, p2.lista_E)
plt.show()


         
          