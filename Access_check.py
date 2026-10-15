username=input("Enter the Username: ")
role=input("Enter the Role: ")
if username=="admin" and role=="administrator":
  print("Full Access")
elif username=="user" and role=="employee":
  print("Limited Access")
else:
  print("Access Denied")