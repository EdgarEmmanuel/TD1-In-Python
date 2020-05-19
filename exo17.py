#PGCD 
#exo 16 et 17


a = int(input("saisir la valeur du nombre a : "))
b = int(input("saisir la valeur du nombre b : "))


if(a>b):
    reste=0
    while(reste!=0):
        reste=a-b
        if(reste==0):
            print("PGCD : ",a)
        svg=reste
        a=b
        b=svg
elif(b>a)
    reste=0
    while(reste!=0):
        reste=b-a 
        if(reste==0):
            print("PGCD : ",b)
        svg=reste
        b=a
        a=svg 
else:
    print("les deux nombres sont egaux ")

print("(",a,",",b,")")