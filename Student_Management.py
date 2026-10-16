name = input("Enter student name: ")

english = float(input("Enter marks for English: "))
maths = float(input("Enter marks for Maths: "))
science = float(input("Enter marks for Science: "))
computer = float(input("Enter marks for Computer: "))
history = float(input("Enter marks for History: "))

if (english < 0 or english > 100 or
    maths < 0 or maths > 100 or
    science < 0 or science > 100 or
    computer < 0 or computer > 100 or
    history < 0 or history > 100):

    print("Error: Marks must be between 0 and 100.")

else:
    total = english + maths + science + computer + history
    percentage = total / 5

    print("\nStudent Name:", name)
    print("Total Marks:", total, "/500")
    print("Percentage:", percentage, "%")

    if (english < 35 or maths < 35 or science < 35 or
        computer < 35 or history < 35):

        print("Grade: E")
        print("Result: FAIL")

    else:
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "E"

        print("Grade:", grade)
        print("Result: PASS")
