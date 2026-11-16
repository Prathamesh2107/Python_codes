marks = {
    "Rahul": 95,
    "Amit": 97,
    "Priya": 98,
    "Sneha": 99
}

sorted_marks = dict(
    sorted(marks.items(), key=lambda item: item[1], reverse=True)
)

print(sorted_marks)