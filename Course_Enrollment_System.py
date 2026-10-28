courses = {
    "Python": (30, 25),
    "AWS": (20, 17),
    "Linux": (15, 13),
    "Docker": (25, 25)
}

for course, details in courses.items():
    maximum_seats, enrolled = details

    if maximum_seats <= 0 or enrolled < 0 or enrolled > maximum_seats:
        status = "Invalid enrollment data"

    else:
        remaining = maximum_seats - enrolled

        if remaining == 0:
            status = "Course Full"
        elif remaining < 5:
            status = "Almost Full"
        else:
            status = "Seats Available"

        print(f"{course}: {remaining} seats remaining")

    print("Status:", status)
