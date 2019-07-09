y,z=input().split()
d=abs(len(z)-len(y))
for i in range(len(y)):
    if(len(z)==1 and z[i] in y):
        break
    if (y[i]!=z[i]):
        d=d+1
print(d)
