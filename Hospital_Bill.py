name = input("Enter patient name: ")
category = input("Enter category (general/semi-private/private): ").lower()
days = int(input("Enter hospital days: "))
medicine = float(input("Enter medicine charges: "))
consultation = float(input("Enter consultation charges: "))

# Validate inputs
if days <= 0 or medicine < 0 or consultation < 0:
    print("Invalid input. Please enter valid amounts and hospital days.")

# Select room charges
elif category == "general":
    room_rate = 1000

elif category == "semi-private":
    room_rate = 2500

elif category == "private":
    room_rate = 5000

else:
    room_rate = 0
    print("Invalid patient category.")

# Calculate bill if category is valid
if category in ["general", "semi-private", "private"] and days > 0 and medicine >= 0 and consultation >= 0:

    room_charges = room_rate * days

    # Calculate room discount
    if days >= 7:
        discount = room_charges * 10 / 100
    else:
        discount = 0

    # Calculate total bill
    total_bill = room_charges - discount + medicine + consultation

    # Display bill
    print("\nPatient Name:", name)
    print("Room Charges: Rs.", room_charges)
    print("Room Discount: Rs.", discount)
    print("Medicine Charges: Rs.", medicine)
    print("Consultation Charges: Rs.", consultation)
    print("Total Bill: Rs.", total_bill)
