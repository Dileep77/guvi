a,b=list(map(int,input().split()))
k=list(map(int,input().split()))
h=[]
for i in range(b):
	u,v=list(map(int,input().split()))
	xor=int(0)
	for z in range(u-1,v):
		xor=xor^(k[z])
	print(xor)
