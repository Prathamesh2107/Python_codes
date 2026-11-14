text = "my name is prathamesh"

frequency = {}

for char in text:

    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)