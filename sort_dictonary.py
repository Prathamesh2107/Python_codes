marks = {
    "Rahul": 85,
    "Amit": 70,
    "Priya": 95,
    "Sneha": 80
}

sorted_marks = dict(
    sorted(marks.items(), key=lambda item: item[1], reverse=True)
)

print(sorted_marks)