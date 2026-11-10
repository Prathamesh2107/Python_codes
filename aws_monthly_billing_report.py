services = {
    "EC2": 4500,
    "S3": 800,
    "RDS": 2500,
    "CloudFront": 700,
    "Lambda": 300
}

total = sum(services.values())

print("========== AWS BILL ==========")

for service, cost in services.items():

    print(service, ": ₹", cost)

print("------------------------------")
print("Total Bill: ₹", total)

if total > 8000:
    print("Alert: Cloud spending is high")

else:
    print("Cloud spending is within budget")