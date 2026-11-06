users = {
    "Amit": "Hello123!",
    "Rahul": "password",
    "Priya": "Python@2026",
    "Sneha": "HELLO123"
}

for username, password in users.items():

    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(not char.isalnum() for char in password)

    score = sum([
        len(password) >= 8,
        uppercase,
        lowercase,
        digit,
        special
    ])

    print("\nUser:", username)

    if score == 5:
        print("Password: Strong")

    elif score >= 3:
        print("Password: Medium")

    else:
        print("Password: Weak")