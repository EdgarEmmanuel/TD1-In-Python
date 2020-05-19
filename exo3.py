#exercice sur les resistances 

R1 = int(input("Saisir la valeur de la resistance R1 : "))
R2 = int(input("Saisir la valeur de la resistance R2 : "))
R3 = int(input("Saisir la valeur de la resistance R3 : "))

#version 1 
r_serie = R1+R2+R3 
r_parallele =  (R1 * R2 * R3) / (R1*R2 + R2*R3 + R1*R3)

#print("Resistance en serie : ",r_serie,"  et resistance en parallele : ",r_parallele)

#version 2

def choix():
    choix = input("faites votre choix : ")
    while(choix!='1' and choix!='2'):
         choix = input("OUPS , faites votre choix entre 1 et 2  : ")
    return choix


choix = choix()

if(choix=="1"):
    print("Resistance en serie : ",r_serie)
else:
    print("resistance en parallele : ",r_parallele)
