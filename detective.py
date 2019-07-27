a=int(input())
k=list(map(int,input().split()))
m=[]
for i in range(len(k)):
	h=[]
	for j in range(i):
		if k[i]>k[j]:
			h.append(k[j])
	sum(h)
	m.append(sum(h))
			
			
		
print(sum(m))
