disks = {
    "/": 55,
    "/home": 90,
    "/var": 35,
    "/backup": 80
}

for partition, usage in disks.items():

    print(partition, "Disk Usage:", usage, "%")

    if usage >= 90:
        print("CRITICAL: Disk almost full")

    elif usage >= 75:
        print("WARNING: Disk usage is high")

    else:
        print("Disk usage is normal")