a=input()
b=input()
if a.find(b)==-1:
  print("-1")
else:
  for i in range(len(a)):
    if b[0]==a[i]:
      print(i)
      break# your code goes here
