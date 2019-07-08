ku,mar=list(map(int,input().split()))
h=[]
for i in range(1,max(ku,mar)+1):
  if ku%i==0 and mar%i==0:
    h.append(i)
print(max(h))# your code goes here
