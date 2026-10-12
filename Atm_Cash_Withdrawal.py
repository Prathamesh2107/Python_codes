num1=int(input("Enter the account balance:"))
num2=int(input("Enter the withdrawal amount:"))
remaining_balance=num1-num2
if num2>0 and num1>num2:
    print("Withdrawal Succesfull")
    print("Remaining Balance=",remaining_balance)
else:
    print("Insufficient Balance")