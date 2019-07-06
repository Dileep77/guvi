dil,eep=list(map(int,input().split()))
h=[]
for i in range(1,dil+1):
  if dil%i==0 and eep%i==0:
    h.append(i)
print(max(h))# your code goes here
