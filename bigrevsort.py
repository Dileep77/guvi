h=int(input())
p=list(map(int,input().split()))
k=3
p.sort(reverse=True)
for i in p:
	print(i,end="")
