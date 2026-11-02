students = {
    "Amit": {"marks": (85, 90, 78), "age": 21},
    "Rahul": {"marks": (30, 45, 60), "age": 22},
    "Priya": {"marks": (95, 92, 98), "age": 23},
    "Sneha": {"marks": (95, 92, 95), "age": 21},
    "Raj": {"marks": (88, 85, 90), "age": 22}
}

results = {}
passed = 0
failed = 0

for name, details in students.items():

    marks = details["marks"]
    total = sum(marks)
    percentage = total / len(marks)

    if any(mark < 35 for mark in marks):
        grade = "F"
        status = "Fail"
        failed += 1

    elif percentage >= 90:
        grade = "A+"
        status = "Pass"
        passed += 1

    elif percentage >= 75:
        grade = "A"
        status = "Pass"
        passed += 1

    elif percentage >= 60:
        grade = "B"
        status = "Pass"
        passed += 1

    else:
        grade = "C"
        status = "Pass"
        passed += 1

    results[name] = {
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status
    }

print("STUDENT PERFORMANCE REPORT")

for name, result in results.items():
    print(f"\nStudent: {name}")
    print("Total:", result["total"])
    print("Percentage:", round(result["percentage"], 2))
    print("Grade:", result["grade"])
    print("Status:", result["status"])

topper = max(
    results,
    key=lambda name: results[name]["total"]
)

print("\nClass Topper:", topper)
print("Passed Students:", passed)
print("Failed Students:", failed)