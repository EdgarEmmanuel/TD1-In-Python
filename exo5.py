#exerciec 5 sur l'addition de 5 variables 

i=0
result=0
while(i<5):
    val = int(input("saisir la valeur du chiffre : "))
    print("Nombre ",i+1," est : ",val)
    result+=val
    i+=1

print("la somme de ces 5 chiffres est : ",result)
