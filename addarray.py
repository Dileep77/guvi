a,b=list(map(int,input().split()))
h=list(map(int,input().split()))
count=0
for i in range(0,len(h)-1):
	for j in range(1,len(h)):
		if h[i]+h[j]==b:
			count=count+1
		else:
			continue
			
if count>=1:
	print("YES")
else:
	print("NO")
