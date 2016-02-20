import random
import os

x=random.randint(1,10)
y=random.randint(1,10)
a=random.randint(1,10)
b=random.randint(1,10)
distance=1

while distance!=0:
    print("1. UP")
    print("2. DOWN")
    print("3. LEFT")
    print("4. RIGHT")
    selection=int(input("Please select an option:"))
    while selection>4 or selection<1:
        print("ERROR!!!")
        print("1. UP")
        print("2. DOWN")
        print("3. LEFT")
        print("4. RIGHT")
        selection=int(input("Please select a CORRECT option [1-4]:"))

    if selection==1:
        if b<10:
            b+=1
        else:
            print("Out of bounds")
    elif selection==2:
         if b>1:
            b-=1
         else:
             print("Out of bounds")
    elif selection==3:
        if a<10:
            a+=1
        else:
            print("Out of bounds")
    elif selection==4:
            if a>1:
                a-=1
            else:
                print("Out of bounds")

    distance=abs(x-a)+abs(y-b)
    print("")
    print ("Distance from treasury:", distance, "steps")

print("Congratulations!!!")
os.system("pause")