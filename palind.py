h=int(input())
temp=h
rev=0
while temp>=1:
  rev=rev*10
  rev=rev+t%10
  t=t/10
if rev==h:
  print("yes")
else:
  print("no")
