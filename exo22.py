array = [1,2,3,1,2,3,4,5,6,7,8,2,3,4,5]

svg = 0 
cpt=0
for i in range (0,len(array)):
    if((array[i+1] is not None)):
        if(array[i]<array[i+1]):
            cpt+=1
            last=array[i+1]
            pos=i+1
        else:
            if(cpt>svg):
                svg=cpt 
                svg2=last
                posi = pos
            pos=0
            cpt=0
            last=0

print("la longeur de la suite est : ",svg)
print("le dernier nombr de la suite est",svg2," , il ets a la position : ",posi)
print("--------- Tableau de la suite Croissante----------")

for j in range((posi-svg),posi):
    print(array[j])