numbers = (237,634,47,3,230,-34,-38,27,-23,-428)

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

