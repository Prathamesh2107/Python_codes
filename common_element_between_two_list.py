a = [10, 20, 30, 40, 70, 90]
b = [30, 40, 50, 10, 70, 80, 90,20]
common=[]
for i in a:
  if i in b:
    common.append(i)
print(common)