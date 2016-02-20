import random
import os
T = [0] * 10
height = 0
p=0
while height <=20:
    p+=1
    x = random.randint(0, 8)
    if T[x]>=T[x+1]
        T[x]+=3
        T[x+1]=T[x]+1
    else:
        T[x]=T[x+1]+3
        T[x+1]+=1
    if T[x]>height:
        height=T[x]

print(p)
os.system("pause")