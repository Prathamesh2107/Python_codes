a=int(input("Enter the Monthly Income: "))
b=int(input("Enter the Room Rent: "))
c=int(input("Enter the Month LightBill: "))
d=int(input("Enter Month Other Expenses: "))
Saving=a-b-c-d
if d>3000:
  print("Your Other Expenses is Above Limit")
  print("Final Savings: ",Saving)
else:
  print("Your Other Expenses are in Limit")
  print("Final Savings: ",Saving)