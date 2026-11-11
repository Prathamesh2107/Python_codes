logs = [
    "INFO Server started",
    "ERROR Database connection failed",
    "WARNING CPU usage high",
    "INFO Backup completed",
    "ERROR Application crashed",
    "WARNING Disk usage high"
]

error_count = 0
warning_count = 0
info_count = 0

for log in logs:

    if "ERROR" in log:
        error_count += 1

    elif "WARNING" in log:
        warning_count += 1

    elif "INFO" in log:
        info_count += 1

print("Error Count:", error_count)
print("Warning Count:", warning_count)
print("Info Count:", info_count)