a=int(input())
i=0
while(1==1):
	i=i+1
	if((2**i)>=a):
		print(min(a-2**(i-1),2**(i)-a))
		break
	
