
array=[9,8,7,6,15,4,3,2,1]

length = len(array)
cpt=1
cpt2=1

#test if c;est croissant 
for j in range(0,length):
    if(j!=length-1):
        if(array[j]<array[j+1]):
            cpt+=1



#test if c'est decroissant 
for k in range(0,length):
    if(k!=length-1):
        if(array[k]>array[k+1]):
            cpt2+=1


if(cpt==length):
    print("le tableau est dans l'ordre croissant ")
elif(cpt2==length):
    print("tableau dans l'ordre decroissant ")
else:
    print("L etableau est dans un ordre quelconque")