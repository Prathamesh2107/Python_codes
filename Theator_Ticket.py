age = int(input("Enter your Age: "))
time = int(input("Enter Show Time (24-hour format): "))

if age < 12:
    ticket = 100

elif age <= 59:
    ticket = 200

else:
    ticket = 100

discount = 0

if time < 12:
    discount = ticket * 20 / 100
    print("Discount: Rs.", discount)
else:
    print("No Discount")

final = ticket - discount
print("Final Price: Rs.", final)
