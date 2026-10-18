numbers = [10, 45, 20, 45, 30, 10, 40]

largest = None
second_largest = None

for num in numbers:
    if largest is None or num > largest:
        second_largest = largest
        largest = num

    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num

if second_largest is None:
    print("No second-largest distinct number exists.")
else:
    print("Largest number:", largest)
    print("Second largest:", second_largest)

