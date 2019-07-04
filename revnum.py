dil=int(input("Enter number: "))
rev=0
while(dil>0):
    dig=dil%10
    rev=rev*10+dig
    dil=dil//10
print("Reverse of the number:",rev)
