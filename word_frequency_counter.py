sentence = "Prathamesh is a cloud engineer also he is clever employee."

words = sentence.lower().split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency:")

for word, count in frequency.items():
    print(word, ":", count)

