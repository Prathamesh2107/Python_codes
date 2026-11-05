orders = {
    "ORD101": ("Amit", 5000, "Placed"),
    "ORD102": ("Rahul", 15000, "Shipped"),
    "ORD103": ("Priya", 25000, "Delivered"),
    "ORD104": ("Sneha", 8000, "Cancelled")
}

for order_id, details in orders.items():

    customer, amount, status = details

    print("\nOrder:", order_id)
    print("Customer:", customer)
    print("Amount:", amount)
    print("Status:", status)

    if status == "Cancelled":
        print("Refund process required")

    elif status == "Delivered":
        print("Order successfully delivered")

    elif status == "Shipped":
        print("Order is on the way")

    elif status == "Placed":
        print("Order is being processed")

    else:
        print("Unknown order status")