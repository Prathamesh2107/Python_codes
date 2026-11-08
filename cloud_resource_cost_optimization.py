instances = {
    "Web-Server": {"cpu": 10, "cost": 5000},
    "Database": {"cpu": 85, "cost": 8000},
    "Backup": {"cpu": 5, "cost": 3000},
    "App-Server": {"cpu": 60, "cost": 6000}
}

for server, details in instances.items():

    cpu = details["cpu"]
    cost = details["cost"]

    print("\nServer:", server)
    print("CPU:", cpu, "%")
    print("Cost: ₹", cost)

    if cpu < 15:
        print("Recommendation: Review instance size or usage")
    elif cpu > 80:
        print("Recommendation: Check capacity requirements")
    else:
        print("Recommendation: No immediate action")