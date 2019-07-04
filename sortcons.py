p=int(input())
a=list(map(int,input().split()))
if p>=1 and p<=100000:
  a.sort()
  for i in a:
    print(i,end=" ")
