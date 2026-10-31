products = {
    "Laptop": (50000, 2),
    "Mouse": (500, 2),
    "Keyboard": (1500, 1),
    "Monitor": (10000, 2)
}

total = 0

for product, details in products.items():
    price, quantity = details
    amount = price * quantity
    total += amount

    print(f"{product}: {price} x {quantity} = {amount}")

if total >= 50000:
    discount_rate = 0.15
elif total >= 25000:
    discount_rate = 0.10
elif total >= 10000:
    discount_rate = 0.05
else:
    discount_rate = 0

discount = total * discount_rate
final_bill = total - discount

print("\nTotal:", total)
print("Discount:", discount)
print("Final bill:", final_bill)

