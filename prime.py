a=int(input())# your code goes here
c=bin(a)

if a==10:
	print("no")
elif c[2]=='1' and c[-1]=='1':
	print("yes")
else:
	print("no")
