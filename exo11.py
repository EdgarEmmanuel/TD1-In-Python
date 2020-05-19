def calcul(a,b,c):
    res = 0 
    if(c=="+"):
        res=a+b 
        print(" a + b  le resultat est  ",res)
    elif(c=="/" or c=="%"):
        if(b!=0):
            if(c=="/"):
                res=a/b
            else:
                print(" a % b  est egal a ")
                res=a%b
                print("resultat = ",res)
        else:
            print("resultat est impossible le nombre b est egal a zero !!!")
    elif(c=="*"):
        res=a*b
        print(" a * b  le resultat est  ",res)
    else:
        print("signe inconnu pour une operation!!!!")


a = int(input("saisir la valeur du nombre a :"))
b = int(input("saisir la valeur du nombre b :"))
c = input("saisir le signe d el'operation : ")


calcul(a,b,c)