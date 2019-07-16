k=int(input())
l=list(map(int,input().split()))
p=[]
for i in range(k):
	if (l[i] not in l[i+1:]) and (l[i] not in p):
		p.append(l[i])
		print(l[i])
		break
	else:
		print(l[-1])
		break
