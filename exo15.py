#additioner une suite de nombre 



a = int(input("saisir le nombre de chiffre que vous souhaitez saisir : "))

somme=0
for i in range(0,a):
    val=int(input("saisir la valeur : "))
    print("valeur ",i+1," est : ",val)
    somme+=val

print("La somme de tous ces chiffres est : ",somme)