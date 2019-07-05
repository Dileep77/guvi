def Repeat(x): 
	_size = len(x) 
	repeated = [] 
	for i in range(_size): 
		k = i + 1
		for j in range(k, _size): 
			if x[i] == x[j] and x[i] not in repeated: 
				repeated.append(x[i]) 
	return repeated 

n=int(input())
list1 = list(map(int,input().split()))
li2=Repeat(list1)
for i in li2:
	print(i,end=" ")
