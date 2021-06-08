import numpy as np
import modul as em
import matplotlib.pyplot as plt


sunce = {
  "polozaj" : np.array([0,0]),
  "masa":1.989*10**30,
  "brzina":np.array([0,0]),
  "velicina": 500,
  "ime":"Sunce",
  "boja" : "y"
}

zemlja = {
  "polozaj" : np.array([1.486*10**11,0]),
  "masa":5.9742*10**24,
  "brzina":np.array([0,29783]),
  "velicina": 100,
  "ime" : "Zemlja",
  "boja" : "g"
}

p1 = em.SolarSistem(sunce,zemlja)
p1.plot()
p1.reset()