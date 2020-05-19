#PPCM 

a = int(input("saisir la valeur du nombre a : "))
b = int(input("saisir la valeur du nombre b : "))

pgcd=0
ppcm=0
p1=a*b
reste=0
if(a > b):
    reste=1
    while(reste!=0):
        reste=a-b
        if(reste==0):
            pgcd=a
            ppcm=p1/pgcd
            print("PPCM : ",ppcm)
        svg=reste
        a=b
        b=svg
elif(b > a):
    reste=2
    while(reste!=0):
        reste=b-a 
        if(reste==0):
            pgcd=b
            ppcm=p1/pgcd
            print("PPCM : ",ppcm)
        svg=reste
        b=a
        a=svg 
else:
    print("les deux nombres sont egaux ")

