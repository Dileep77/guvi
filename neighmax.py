a=int(input())
b=list(map(int,input().split()))
sumoo=0
sumee=0
for i in range(a):
	if i%2==0:
		sumoo=sumoo+b[i]
	else:
		sumee+=b[i]
print(max(sumoo,sumee))# your code goes here
