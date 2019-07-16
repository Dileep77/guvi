k=int(input())
l=list(map(int,input().split()))
for i in range(k):
	if i==0:
		min=l[0]
	elif l[i-1]>l[i]:
		min=l[i]
	print(min,end=" ")
