a=list(map(str,input()))
b=list(map(str,input()))
k=[]
l=[]
m=[]
for i in a:
	k.append(ord(i))
for j in b:
	l.append(ord(j))
for p in range(0,len(k)):
	if (((k[p]+l[p])-96)>122):
		m.append(chr(abs((k[p]+l[p])-122)))
	else:
		m.append(chr(abs((k[p]+l[p])-96)))
for i in m:
	print(i,end="")
#for h in range(len(m)):
	#print(chr(h))

	
