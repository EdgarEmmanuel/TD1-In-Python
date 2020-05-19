import math


rayon = int(input("saiir le rayon du cercle : "))

PI = 4*math.atan(1)

print("La surface de ce cercle est : ",(math.pow(rayon,2)*PI))
print("Le perimetre de ce cercle est : ",(2*PI*rayon))