#execrice sur les lpins 
#suite c'est mois = mois_precedent + mois_precedent_precedent


mois_precedent = 2
mois_precedent_precedent = 0
i=0
nombre_lapin = -12

while(nombre_lapin<1000000000):
    nombre_lapin = mois_precedent+mois_precedent_precedent
    mois_precedent_precedent=mois_precedent
    mois_precedent=nombre_lapin
    i+=1
    if(i==12):
        print("Au douzieme mois ,nombre de lapin est : ",nombre_lapin)


print("le nombre de lapins depassera 1 milliard le ",i," mois ")