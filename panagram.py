a=list(map(str,input().strip()))
p="qwertyuiopasdfghjklzxcvbnm"
count=0
for i in p:
	if i in a:
		count+=1
if count==26:
	print("yes")
else:
	print("no")
