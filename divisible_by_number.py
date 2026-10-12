a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
if a%3==0 and b%3==0:
  print("both numbers divisible by 3")
elif a%3!=0 and b%3==0:
  print("a is not divisible by 3 and b is divisible by 3")
elif a%3==0 and b%3!=1:
  print("a is divisible by 3 and b is not divisible by 3")
else:
  print("both are not divisible by 3")
  