a=list(map(str,input()))
k=[]
for i in a:
	if i.islower()==True:
		k.append(i.upper())
	elif i.isupper()==True:
		k.append(i.lower())

for h in k:
	print(h,end="")
