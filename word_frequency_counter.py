sentence = "My name is Prathamesh Chormale. My nickname is Bholu"

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

