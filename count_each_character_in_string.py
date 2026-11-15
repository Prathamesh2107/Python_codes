text = "i am a cloud engineer"

frequency = {}

for char in text:

    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)