

a = int(input("saisir le nombre secret : "))

b = int(input("allez utiisateur 2 , Devinez le nombre secret "))

while(b!=a):
    if(b>a):
        b=int(input("Nombre trop grand ,essaye encore : "))
    if(b<a):
        b=int(input("nombre trop petit , try again : "))


print("enfin trouve , le nombre eteait effectivement : ",a)