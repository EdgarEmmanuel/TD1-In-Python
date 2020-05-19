
import math

#version 1
heure_depart = int(input("Entrez l'heure de depart en entier : "))
minutes_depart = int(input("Entrez minutes de depart en entier : "))

heure_arrivee = int(input("Entrez l'heure d'arrivee en entier : "))
minutes_arrive = int(input("Entrez minutes d'arrivee en entier : "))

total_minutes_depart = (heure_depart*60)+minutes_depart
total_minutes_arrivee = (heure_arrivee*60)+minutes_arrive


# duree_trajet_en_minutes = total_minutes_arrivee - total_minutes_depart


# duree_en_heure = math.floor(duree_trajet_en_minutes / 60)
# duree_en_minutes = duree_trajet_en_minutes % 60

# print("La duree du trajet est ",duree_en_heure,"h ",duree_en_minutes,"mn")


#version 2 ici l'arrivee a lieu le lendemain 

duree_journee= 24*60


duree_trajet_Total = (duree_journee - total_minutes_depart) + total_minutes_arrivee

during_in_hours = math.floor(duree_trajet_Total/60)
during_in_minutes = duree_trajet_Total % 60

print("la duree de ce vol a ete de  ",during_in_hours,"h",during_in_minutes,"mn")

