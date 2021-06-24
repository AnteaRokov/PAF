import matplotlib.pyplot as plt
import zadatak1 as z 

h1 = z.Bullet(2, 100)
h1.move(0.01)    

plt.figure("Hitac")
fig = plt.subplot()
plt.subplot(2,1,1)
plt.plot(h1.t_lista,h1.h_lista)
plt.xlabel("t [s]")
plt.ylabel("h [m]")
plt.title("h-t graf")
plt.subplot(2,1,2)
plt.plot(h1.t_lista,h1.v_lista)
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")
plt.title("v-t graf")
plt.show()

plt.plot(h1.X_lista,h1.h_lista)
plt.xlabel("x [m]")
plt.ylabel("h [m]")
plt.title("x-h graf")
plt.show()
