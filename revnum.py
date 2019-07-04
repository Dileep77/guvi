dil=int(input("Enter number: "))
kev=0
while(dil>0):
    pig=dil%10
    kev=kev*10+pig
    dil=dil//10
print(kev)
