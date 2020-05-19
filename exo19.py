#somme des articles 

prices=[]
a = int(input("Combien de prix voulez vous saisir : "))
somme=0
for j in range(0,a):
    val=int(input("saisir le prix du produit : "))
    while((val%10)!=0):
        val=int(input("Oups le prix doit se terminer par zero , saisir le prix du produit : "))
    prices.append(val)
    somme+=val


print("--------- L es prix des produits dans votre panier-------")
for j in range(0,a):
    print(str(prices[j])+" FCFA")


print("Facture : "+str(somme)+" FCFA")
