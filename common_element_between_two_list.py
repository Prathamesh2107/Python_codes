a = [10, 20, 30, 40]
b = [30, 40, 50, 60]
common=[]
for i in a:
  if i in b:
    common.append(i)
print(common)