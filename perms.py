a=int(input())
def fact(n):
	if n == 1:
		return n
	elif(n==0):
		return 1
	else:
		return n*fact(n-1)
		
c=fact(a)/fact(a-2)
print(int(c/2))
