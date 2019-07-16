a,b=list(map(str,input().split()))
for i in range(len(a)):
	if i<=len(a)-int(b):
		print(a[i:i+int(b)],end=" ")
