
p,q=map(int,input().split())
for i in range(p,q):
  temp=a
  arm=0
  while a>=1:
    n=a%10
    arm=arm+n**3
    a=int(a/10)
if temp==arm:
  print(temp,end="")
