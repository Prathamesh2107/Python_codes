backups = {
    "Web-Server": "completed",
    "Database": "failed",
    "App-Server": "completed",
    "File-Server": "pending"
}

for server, status in backups.items():

    if status == "completed":
        print(server, "- Backup Successful")

    elif status == "failed":
        print(server, "- Backup Failed")

    else:
        print(server, "- Backup Pending")