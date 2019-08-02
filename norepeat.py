a=int(input())
b=list(map(int,input().split()))
k=[]
for i in range(len(b)):
	if b[i] in b[i+1:]:
		k.append(b[i])
for j in range(len(b)):
	if b[j] not in k:
		print(b[j])
