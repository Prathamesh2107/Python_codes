shopping=int(input("Enter the Shopping Amount: "))
if shopping>=10000:
  discount=shopping*25/100
  final_price=shopping-discount
  print("Discount: Rs.",discount)
  print("Final Price: Rs.",final_price)
elif shopping>=5000 and shopping<10000:
  discount=shopping*15/100
  final_price=shopping-discount
  print("Discount: Rs.",discount)
  print("Final Price: Rs.",final_price)
else:
  discount=shopping*0/100
  final_price=shopping-discount
  print("No Discount: Rs.",discount)
  print("Final Price: Rs.",final_price)