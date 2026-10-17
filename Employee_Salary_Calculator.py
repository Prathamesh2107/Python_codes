name = input("Enter Employee Name: ")
basic = float(input("Enter Basic Salary: "))
experience = int(input("Enter Years of Experience: "))
rating = int(input("Enter Performance Rating (1-5): "))

if basic < 0 or experience < 0 or rating < 1 or rating > 5:
    print("Invalid Input")

else:
    # Calculate HRA
    if basic >= 50000:
        hra = basic * 20 / 100
    elif basic >= 25000:
        hra = basic * 15 / 100
    else:
        hra = basic * 10 / 100

    # Calculate Experience Bonus
    if experience >= 10:
        exp_bonus = basic * 15 / 100
    elif experience >= 5:
        exp_bonus = basic * 10 / 100
    else:
        exp_bonus = basic * 5 / 100

    # Calculate Performance Bonus
    if rating == 5:
        performance_bonus = 5000
    elif rating == 4:
        performance_bonus = 3000
    elif rating == 3:
        performance_bonus = 1000
    else:
        performance_bonus = 0

    # Calculate Final Salary
    final_salary = basic + hra + exp_bonus + performance_bonus

    # Display Salary Details
    print("\nEmployee Name:", name)
    print("Basic Salary: Rs.", basic)
    print("HRA: Rs.", hra)
    print("Experience Bonus: Rs.", exp_bonus)
    print("Performance Bonus: Rs.", performance_bonus)

