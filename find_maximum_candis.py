candies = [2, 3, 5, 1, 3]
extraCandies = 3

ans = []
maximum = candies[0]

for i in candies:
    if i > maximum:
        maximum = i

# Check each kid
for i in candies:
    if i + extraCandies >= maximum:
        ans.append(True)
    else:
        ans.append(False)

print(ans)