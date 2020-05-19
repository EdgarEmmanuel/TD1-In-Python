import math 

#exercice sur les exposants 

number = int(input("saisir la valeur du nombre : "))
exposant = int(input("saisir la valeur de l'exposant : "))

#with function pow
#print("le resulat  est egal a : ",math.pow(number,exposant))


#with the while loop 
result =1
i=1
while(i<=exposant):
    result=result*number
    i+=1

print("resulat est egal a : ",result)