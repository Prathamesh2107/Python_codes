servers = {
    "Web-Server": {
        "CPU": 25,
        "Memory": 10,
        "Disk": 10,
        "Status": "stopped"
    },

    "Database": {
        "CPU": 95,
        "Memory": 92,
        "Disk": 90,
        "Status": "running"
    },

    "Backup-Server": {
        "CPU": 20,
        "Memory": 30,
        "Disk": 50,
        "Status": "stopped"
    }
}

def generate_report():

    critical_count = 0
    healthy_count = 0

    for server, details in servers.items():

        print("\nServer:", server)

        if details["Status"] == "stopped":
            print("Status: STOPPED")
            critical_count += 1
            continue

        cpu = details["CPU"]
        memory = details["Memory"]
        disk = details["Disk"]

        if cpu >= 90 or memory >= 90 or disk >= 90:

            print("Health: CRITICAL")
            critical_count += 1

        else:
            print("Health: HEALTHY")
            healthy_count += 1

    print("\n========== FINAL REPORT ==========")
    print("Healthy Servers:", healthy_count)
    print("Critical/Stopped Servers:", critical_count)

generate_report()