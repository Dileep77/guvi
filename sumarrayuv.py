
a,b=input().split()
h=list(map(int,input().split()))
for p in range(int(b)):
	u,v=input().split()
	sum=0
	for z in range(int(u)-1,int(v)):
		sum=sum+h[z]
	print(sum)
	continue
