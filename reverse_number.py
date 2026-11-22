x = 3674
k=0
while x>0:
  d=x%10
  k=k*10+d
  x=x//10
print(k)