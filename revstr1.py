a=list(map(str,input().split()))
h=[]
for i in a:
	k=i[::-1]
	h.append(k)
for j in h:
	print(j,end=" ")
