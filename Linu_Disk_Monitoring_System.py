disks = {
    "/": 85,
    "/home": 60,
    "/var": 95,
    "/backup": 40
}

for partition, usage in disks.items():

    print(partition, "Disk Usage:", usage, "%")

    if usage >= 90:
        print("CRITICAL: Disk almost full")

    elif usage >= 75:
        print("WARNING: Disk usage is high")

    else:
        print("Disk usage is normal")