name = input("Enter student name: ")
age = int(input("Enter age: "))
percentage = float(input("Enter 12th-grade percentage: "))
entrance = float(input("Enter entrance exam score out of 100: "))
income = float(input("Enter annual family income: "))

tuition_fee = 100000

# Validate inputs
if age <= 0 or percentage < 0 or percentage > 100 or entrance < 0 or entrance > 100 or income < 0:
    print("Invalid input")

else:
    # Engineering Admission Eligibility
    if age >= 17 and percentage >= 60 and entrance >= 70:
        print("\nAdmission Status: Eligible for Engineering Admission")
    else:
        print("\nAdmission Status: Not Eligible for Engineering Admission")

    # Scholarship Eligibility
    if percentage >= 85 and entrance >= 80 and income < 300000:
        print("Scholarship Status: Eligible for Scholarship")
    else:
        print("Scholarship Status: Not Eligible for Scholarship")

    # Calculate Merit Discount
    if percentage >= 90:
        discount = tuition_fee * 25 / 100
    elif percentage >= 75:
        discount = tuition_fee * 10 / 100
    else:
        discount = 0

    final_fee = tuition_fee - discount

    # Display Fee Details
    print("\nAnnual Tuition Fee: Rs.", tuition_fee)
    print("Merit Discount: Rs.", discount)
    print("Final Tuition Fee: Rs.", final_fee)
