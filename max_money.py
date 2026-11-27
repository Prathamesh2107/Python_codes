accounts = [
    [10, 20, 30],
    [40, 50, 10],
    [5, 5, 5]
]

wealth=0
for i in accounts:
  temp=0
  
  for j in i:
    temp+=j
    
  if wealth<temp:
      wealth=temp
print(wealth)