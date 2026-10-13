salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years >= 10:
  percentage = 20
elif years >= 5:
  percentage = 10
else:
  percentage = 5

bonus = salary * percentage / 100

print("Bonus: Rs.", bonus)
