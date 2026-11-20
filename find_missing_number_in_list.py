numbers = [9, 8, 2, 7, 3, 6, 5, 1, 4, 10, 11, 12, 13, 15]

n = 15

total = n * (n + 1) // 2

missing = total - sum(numbers)

print("Missing Number:", missing)