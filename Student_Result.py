subject1=int(input("Enter the Subject1 Marks="))
subject2=int(input("Enter the Subject2 Marks="))
subject3=int(input("Enter the Subject3 Marks="))
average=(subject1+subject2+subject3)/3
print("Average=",average)

if subject1>=35 and subject2>=35 and subject3>=35 and average>=40:
  print("You are pass")
else:
  print("you are fail")