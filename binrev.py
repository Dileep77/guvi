a=int(input())
k=list(map(int,input().split()))
k.sort(reverse=True)
for i in range(len(k)):
	print(k[i])
