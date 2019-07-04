n=int(input())
a=list(map(int,input().split()))
a.sort()
if n%2==0:
  m=int(a[n/2]+a[(n/2)-1])
else
  m=int(a[(n//2)])
print(m)
