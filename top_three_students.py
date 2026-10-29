students = {
    "Prathamesh": 97,
    "Shraddha": 92,
    "Priya": 88,
    "Sneha": 95,
    "Raj": 88
}

remaining = students.copy()

for rank in range(1, min(3, len(remaining)) + 1):
    highest_name = None
    highest_marks = None

    for name, marks in remaining.items():
        if highest_marks is None or marks > highest_marks:
            highest_marks = marks
            highest_name = name

    print(f"{rank}. {highest_name}: {highest_marks}")
    del remaining[highest_name]

