numbers = [9, 8, 2, 3, 6, 5, 1, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

n = 20

total = n * (n + 1) // 2

missing = total - sum(numbers)

print("Missing Number:", missing)