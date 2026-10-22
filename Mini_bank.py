admin=(input("Enter the username="))
Pass=int(input("Enter the Password="))
username="prathamesh"
password=2107
if username==admin and password==Pass:

  print("""
       1.Add Balance
       2.Withdraw Amount
       3.Check Balance""")

  acc=50000

  choice=int(input("Enter the Choice="))

  if choice==1:
    deposit=int(input("Enter the amount="))
    if deposit>0:
      acc=acc+deposit
      print("Successfully Deposited")
      print("Current Balance=",acc)
    else:
      print("Enter the positive amount=")

  elif choice==2:
    withdraw=int(input("Enter the withdraw amount="))
    if withdraw>0:
      if withdraw<acc:
        acc=acc-withdraw
        print("Amount is been withdraw=",withdraw)
        print("remaining balance=",acc)
      else:
        print("Insufficient Amount=")
    else:
      print("Negative Amount is not allowed")

  elif choice==3:
    print("your Account Balance=",acc)

  else:
    print("Please Enter valid Choice 1,2,3 only")
else:
  print("Enter Valid Username and Password")
    
  