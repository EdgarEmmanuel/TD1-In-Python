#pour 1 a 10 

import sys

for i in range (1,11):
    nb=0
    while(nb<i):
        sys.stdout.write(str(i))
        nb+=1
    print(" ")