accounts = [
    [10, 90, 30],
    [40, 60, 10],
    [54, 55, 35]
]

wealth=0
for i in accounts:
  temp=0
  
  for j in i:
    temp+=j
    
  if wealth<temp:
      wealth=temp
print(wealth)