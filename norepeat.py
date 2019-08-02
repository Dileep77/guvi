a=int(input())
b=list(map(int,input().split()))
for i in range(len(b)):
	if b[i] not in b[i+1:]:
		print(b[i])
		break
