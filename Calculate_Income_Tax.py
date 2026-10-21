income=int(input("Enter Annual Income: "))
if income<=400000:
  tax=income*0/100
  print("Tax Amount: Rs.",tax)
elif income>400000 and income<=800000:
  tax=income*5/100
  print("Tax Amount: Rs.",tax)
else:
  tax=income*10/100
  print("Tax Amount: Rs.",tax)