ports = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "Application",
    53: "DNS",
    67: "DHCP"
}

port_status = {
    22: "open",
    80: "open",
    443: "open",
    3306: "closed",
    8080: "open",
    53: "closed",
    67: "open"
}

for port, service in ports.items():

    print("\nPort:", port)
    print("Service:", service)

    if port_status[port] == "open":
        print("Status: Available")

    else:
        print("Status: Unavailable")