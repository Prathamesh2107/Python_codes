salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years >= 5:
  percentage = 40
elif years >= 2:
  percentage = 20
else:
  percentage = 10

bonus = salary * percentage / 100

print("Bonus: Rs.", bonus)
