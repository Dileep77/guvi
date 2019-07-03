h=int(input())
temp=h
rev=0
while temp>=1:
  rev=rev*10
  rev=rev+temp%10
  temp=temp/10
if rev==h:
  print("yes")
else:
  print("no")
