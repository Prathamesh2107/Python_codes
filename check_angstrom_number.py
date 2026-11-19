num = 153

temp = num
total = 0
power = len(str(num))

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")