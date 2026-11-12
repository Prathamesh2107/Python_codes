numbers = [9, 8, 2, 3, 6, 5, 1, 4]

n = 9

total = n * (n + 1) // 2

missing = total - sum(numbers)

print("Missing Number:", missing)