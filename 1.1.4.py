#!/usr/bin/env python3

from math import pi

class Cercle:
   
   # Attribut
   rayon = ""
   
   def __init__(self, rayon):
     self.rayon = int(rayon)
     
   def air(self):
      return pi * self.rayon ** 2
   
   def perimetre(self):
      return 2 * pi * self.rayon


rayon = input("Saisissez le rayon du cercle : ")
cercle = Cercle(rayon)
print ("Air : " + str(cercle.air()))
print ("Perimetre : " + str(cercle.perimetre()))
