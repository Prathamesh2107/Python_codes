income=int(input("Enter Annual Income: "))
if income<=300000:
  tax=income*0/100
  print("Tax Amount: Rs.",tax)
elif income>300000 and income<=600000:
  tax=income*5/100
  print("Tax Amount: Rs.",tax)
else:
  tax=income*10/100
  print("Tax Amount: Rs.",tax)