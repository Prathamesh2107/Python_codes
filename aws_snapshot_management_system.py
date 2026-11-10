snapshots = {
    "snap-101": {"volume": "vol-101", "status": "completed"},
    "snap-102": {"volume": "vol-102", "status": "pending"},
    "snap-103": {"volume": "vol-103", "status": "failed"}
}

for snapshot_id, details in snapshots.items():

    print("\nSnapshot:", snapshot_id)

    if details["status"] == "completed":
        print("Backup successful")

    elif details["status"] == "pending":
        print("Backup is processing")

    else:
        print("Backup failed - Investigation required")