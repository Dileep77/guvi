a=int(input())
b=list(map(int,input().split()))
k=[]
for i in range(0,len(b)):
	if i%2==0 and b[i]%2==1:
		k.append(b[i])
	if i%2==1 and b[i]%2==0:
		k.append(b[i])
print(*k)
