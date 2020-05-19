#exercice sur les coordonnes 
import math

x1 = int(input("Saisir la valeur x1 du point A : "))
y1 = int(input("Saisir la valeur y1 du point A : "))
x2 = int(input("Saisir la valeur x2 du point B : "))
y2 = int(input("Saisir la valeur y2 du point B : "))


distance = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
print("La distance entre ces deux points est : ",distance)