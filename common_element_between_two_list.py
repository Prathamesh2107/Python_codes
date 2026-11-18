a = [10, 20, 30, 40, 70, 90]
b = [30, 40, 50, 60, 70, 80, 90]
common=[]
for i in a:
  if i in b:
    common.append(i)
print(common)