numbers = (10, -5, 0, 8, -3, 7, 12, -2)

positive = []
negative = []
even = []
odd = []
zeros = 0

for number in numbers:
    if number > 0:
        positive.append(number)
    elif number < 0:
        negative.append(number)
    else:
        zeros += 1

    if number != 0:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

print("Positive:", tuple(positive))
print("Negative:", tuple(negative))
print("Even:", tuple(even))
print("Odd:", tuple(odd))
print("Zeros:", zeros)

