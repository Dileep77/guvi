h=int(input())
p=list(map(int,input().split()))
kh=3
p.sort(reverse=True)
for i in p:
	print(i,end="")
