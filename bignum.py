a,b,c=map(int,input().split())
if a>b and a>c:
  largest=a
elif b>c and b>a:
  largest=b
else:
  largest=c
print(largest)
