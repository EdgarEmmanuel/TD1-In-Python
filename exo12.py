#nombre parfait 



a = int(input("saisir un nomre : "))

print("------ Vous voulez savoir si il est parfait ? ----------")

somme=0
for j in range(1,a):
    if(a%j==0):
        somme+=j


if(somme==a):
    print("Eh bien oui le nombre ",a," est bien un nombre parfait")
else:
    print("votre nombre est imparfait aha (-_-) ")