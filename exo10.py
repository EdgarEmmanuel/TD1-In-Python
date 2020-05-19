#trier la liste 

numbers = []


for i in range(0,3):
    val = int(input("saisir la valeiur du nombre : "))
    numbers.append(val)

print("---------Affichage du tableau Avant tri  ------------")

for j in range(0,len(numbers)):
    print(numbers[j]," | ")


print("--------- Apres tri par ordre croissant ----------")

svg=0

for j in range(0,len(numbers)):
    for k in range(j,len(numbers)):
        if(numbers[j]>numbers[k]):
            svg = numbers[j]
            numbers[j]=numbers[k]
            numbers[k]=svg


for j in range(0,len(numbers)):
    print(numbers[j]," | ")