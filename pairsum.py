p,k=map(int,input().split())
q=list(map(int,input().split()))[:p]
count=0
for i in range(0,len(q)-1):
  for sec in range(i+1,len(q)-1):
    if(q[i]+q[sec]==k):
      count+=1  
#print(count) 
#print(j)   
if count==1:
  print("yes")
else:
  print("no")
