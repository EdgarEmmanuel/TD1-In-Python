#verifier si date est valide 

annee = 2020

jour = int(input("saisir la valeur le jour de la date en entier : "))
mois = int(input("saisir le mois de la date en entier : "))


if(mois==2 and jour>29):
    print("cette date est invalide")
elif(jour>=1 and jour<=31 and mois>=1 and mois <=12):
    print(jour,"/",mois,"/",annee)
    print("date valide ")
else:
    print("Date invalide verifiez bien ")
