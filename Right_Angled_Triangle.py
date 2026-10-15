a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid side lengths")

elif a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")

else:
    if a >= b and a >= c:
        longest = a
        x = b
        y = c

    elif b >= a and b >= c:
        longest = b
        x = a
        y = c

    else:
        longest = c
        x = a
        y = b

    if longest ** 2 == x ** 2 + y ** 2:
        print("Right-angled triangle")
    else:
        print("Not a right-angled triangle")
