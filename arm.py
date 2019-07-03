
a=int(raw_input())
temp=a
arm=0
while a>0:
  n=a%10
  arm=arm+n**3
  a=a/10
if temp==arm:
  print("yes")
else:
  print("no")
