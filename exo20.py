
#methode 1
numbers = []

plus_grand=0
for i in range(0,10):
    val=int(input("saisir la valeur du nombre : "))
    numbers.append(val)
    if(val>plus_grand):
        plus_grand=val
        posi=i

print("le plus grand nombre est "+str(plus_grand)+" et sa position est "+str(posi))

##methode 2

# for i in range(0,10):
#     val=int(input("saisir la valeur du nombre : "))
#     numbers.append(val)

# #tri dans l'ordre croissant 
# svg=0
# for i in range(0,10):
#     for j in range(i,10):
#         if(numbers[i]>numbers[j]):
#             svg=numbers[i]
#             numbers[i]=numbers[j]
#             numbers[j]=svg


# #et on recupere la dernier valeur 

# print("la valeur la plus grande du tableau est : ",numbers[9])


#methode 2

