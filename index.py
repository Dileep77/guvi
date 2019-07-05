n=int(input())
mat=[]
li2=list(map(int,input().split()))
for i in range(0,len(li2)):
	if i==li2[i]:
		mat.append(li2[i])

if mat==[]:
	print("-1")
else:
	mat.sort()
	for k in mat:
		print(k,end=" ")
