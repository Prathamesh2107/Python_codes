num=int(input("Enter the Number="))
if num%3==0 and num%5==0:
  print("Divisible by both 3 & 5")
elif num%3!=0 and num%5!=0:
  print("Not Divisible by both 3 & 5")
elif num%3!=0 and num%5==0:
  print("Not Divisible by 3 and Divisible by 5")
else:
  print("Divisible by 3 & not divisible by 5")