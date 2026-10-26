students = (
    ("Rushi", (85, 90, 78)),
    ("Devidas", (78, 50, 60)),
    ("Pratham", (95, 92, 98)),
    ("Sneha", (79, 70, 75)),
    ("Hitesh", (73,75,37))
)

for name, marks in students:
    total = sum(marks)
    percentage = total / len(marks)

    if any(mark < 35 for mark in marks):
        result = "FAIL"
        grade = "F"
    elif percentage >= 75:
        result = "PASS"
        grade = "A"
    elif percentage >= 60:
        result = "PASS"
        grade = "B"
    else:
        result = "PASS"
        grade = "C"

    print(f"\nStudent: {name}")
    print(f"Total: {total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Result: {result}")
    print(f"Grade: {grade}")
