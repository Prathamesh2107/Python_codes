servers = {
    "EC2-01": (35, 45, 50),
    "EC2-02": (85, 90, 75),
    "EC2-03": (46, 38, 25),
    "EC2-04": (60, 55, 80),
    "EC2-05": (10, 20, 25)
}

for server, metrics in servers.items():

    cpu, memory, disk = metrics

    print("\nServer:", server)

    if any(value < 0 or value > 100 for value in metrics):
        print("Invalid monitoring data")
        continue

    if cpu >= 95 or memory >= 95 or disk >= 95:
        status = "CRITICAL"

    elif cpu >= 80 or memory >= 80 or disk >= 80:
        status = "WARNING"

    else:
        status = "HEALTHY"

    print("CPU:", cpu, "%")
    print("Memory:", memory, "%")
    print("Disk:", disk, "%")
    print("Server Status:", status)

    if status == "CRITICAL":
        print("Action: Immediate investigation required")

    elif status == "WARNING":
        print("Action: Monitor server closely")

    else:
        print("Action: No action required")