cost=int(input("Enter the cost price="))
selling=int(input("Enter the selling price="))
profit=selling-cost
loss=cost-selling
if selling>cost:
  print("Profit=",profit)
elif cost>selling:
  print("Loss=",loss)
else:
  print("No Profit,No Loss")