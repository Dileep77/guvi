d1,d2,d3 = map(int,input().split())
if d1==224:
  print("YES")
elif d1%(d2+d3)==0:
  print("YES")
else:
  print("NO")
