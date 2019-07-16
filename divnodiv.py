a,b=list(map(int,input().split()))
sum=0
count=0
while(True):
  sum=sum+b
  count+=1
  if sum==a:
    print(count)
    break
