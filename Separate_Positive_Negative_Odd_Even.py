numbers = (72,-238,38,302,-28,-273,730,-387,37,-18)

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

