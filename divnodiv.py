a,b=list(map(int,input().split()))
sum=0
count=0
if a==0:
	print("0")
	
else:
	if a>=b:
		while(True):
			sum=sum+b
			count+=1
			if sum==a:
				print(count)
				break
