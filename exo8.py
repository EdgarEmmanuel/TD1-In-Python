#resolution equation du second degres

import math

a = int(input("saisir la valeur de a: "))
b=int(input("saisir la valeur de b : "))
c = int(input("saisir la valeur de c: "))

print("votre equation est ",a,"x^2 +",b,"x + ",c)

discriminant = math.pow(b,2) - (4*a*c)

if(discriminant>0):
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(" X1 = ",x1)
    print(" X2 = ",x2)
elif(discriminant==0):
    x1 = (-b) / (2*a)
    print("Discriminant est egal a : ",discriminant)
    print("resultat de l'equation est : ",x1)
else:
    print("pa sde solution le discriminant est negatif ")