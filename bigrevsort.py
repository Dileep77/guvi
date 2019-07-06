a=int(input())
k=list(map(int,input().split()))
k.sort(reverse=True)
for i in k:
	print(i,end=" ")
