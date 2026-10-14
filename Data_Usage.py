data = float(input("Enter data usage in GB: "))

if data < 0:
    print("Invalid data usage")

elif data <= 1:
    print("Data charge: Rs. 50")

elif data <= 3:
    print("Data charge: Rs. 100")

else:
    print("Data charge: Rs. 200")
