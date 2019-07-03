a=input()
b=input()
c=input()
if a>b and a>c:
  largest=a
elif b>c and b>a:
  largest=b
else:
  largest=c
print(largest)
