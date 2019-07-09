a=int(input())
n=list(map(int,input().split()))
h=0
for i in range(0,a-2):
  for j in range(1,a-1):
    for k in range(2,a):
      if(n[i]<n[j] and n[j]<n[k]):
        h+=1
print(h)
