import math
class Bullet:
    def __init__(self, h0, v0):
        self.x = 0
        self.h0 = h0
        self.v0 = v0
        self.h = self.h0
        self.v = self.v0
        self.t_brojac = 0 
    

        theta = 0
        self.thetarad = theta*math.pi/180

        self.v_lista = []
        self.vx_lista = []
        self.vy_lista = []
        self.h_lista = []
        self.t_lista = []
        self.h_lista = []
        self.X_lista = []

        self.vx = self.v0 * math.cos(self.thetarad)
        self.vy = self.v0 * math.sin(self.thetarad)

        self.v_lista.append(self.v)
        self.h_lista.append(self.h)
        self.t_lista.append(self.t_brojac)
        self.X_lista.append(self.x)

        self.vx_lista.append(self.vx)
        self.vy_lista.append(self.vy)


        return print('Pocetna visina iznosi: {}, a brzina iznosi: {}'.format(self.h, self.v))

    def uspori_ili_ubrzaj_metak(self, v1):
        pitanje = int(input('Ako zelite usporiti metak unesite 1, a ako zelite ubrzati metak unesite bilo koji drugi prirodni broj: '))

        if pitanje == 1:
            self.v0 = self.v0 - v1
            self.v = self.v0

        else:
            self.v0 = self.v0 + v1
            self.v = self.v0

        return self.v

    def smanji_ili_povecaj_visinu(self, h1):
        pitanje = int(input('Ako zelite smanjiti visinu metka metak unesite 1, a ako zelite povecati visinu metka unesite bilo koji drugi prirodni broj: '))

        if pitanje == 1:
            self.h0 = self.h0 - h1
            self.h = self.h0
        
        else:
            self.h0 = self.h0 + h1
            self.h = self.h0

        return self.h

    def move(self, delta_t):  
        
                                               #racunam kao kosi hitac tj da je vx const                
        while self.h >= 0:

            self.vy = self.vy + (-9.81) * delta_t

            self.x = self.x + self.vx * delta_t
            self.X_lista.append(self.x)

            self.h = self.h + self.vy * delta_t
            self.h_lista.append(self.h)

            self.v = math.sqrt(self.vx**2 + self.vy**2)
            self.v_lista.append(self.v),

            self.t_brojac = self.t_brojac + delta_t
            self.t_lista.append(self.t_brojac)

        return self.v_lista , self.h_lista, self.X_lista, self.t_lista


    def velocity_to_hit_target(self, l, h, y_vel_mete): 
        self.r_meta = y_vel_mete/2
        self.v0 = 0
        meta_je_pogodena = False
        self.vx = self.v0 * math.cos(self.thetarad)
        self.vy = self.v0 * math.sin(self.thetarad)
        
        while True:
            self.move(delta_t)

            D = math.sqrt((self.x - l )**2 + (self.h0 - h )**2)

            if D <= self.r_meta:
                meta_je_pogodena = True
                break
            break
        return print('Brzina kojom je meta pogodena iznosi: {}'.format(self.v))



    def move_s_otporom_zraka(self, delta_t, m, k):  
        
                                               #racunam kao kosi hitac tj da je vx const                
        while self.h >= 0:

            self.vy = self.vy - (9.81 + (k*self.vy)/m ) * delta_t 

            self.x = self.x + self.vx * delta_t
            self.X_lista.append(self.x)

            self.h = self.h + self.vy * delta_t
            self.h_lista.append(self.h)

            self.v = math.sqrt(self.vx**2 + self.vy**2)
            self.v_lista.append(self.v),

            self.t_brojac = self.t_brojac + delta_t
            self.t_lista.append(self.t_brojac)

        return self.v_lista , self.h_lista, self.X_lista, self.t_lista


    def velocity_to_hit_target_s_otporom_zraka(self, l, h, y_vel_mete): 
        self.r_meta = y_vel_mete/2
        self.v0 = 0
        meta_je_pogodena = False
        self.vx = self.v0 * math.cos(self.thetarad)
        self.vy = self.v0 * math.sin(self.thetarad)
        
        while True:
            self.move_s_otporom_zraka(delta_t, m, k)

            D = math.sqrt((self.x - l )**2 + (self.h0 - h )**2)

            if D <= self.r_meta:
                meta_je_pogodena = True
                break
            break
        return print('Brzina kojom je meta pogodena iznosi: {}'.format(self.v))


    
        



            

      




    

