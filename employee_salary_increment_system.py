employees = {
    "Amit": 12000,
    "Rahul": 25000,
    "Priya": 45000,
    "Sneha": 18000,
    "Raj": -500
}

updated_salaries = {}

for name, salary in employees.items():
    if salary <= 0:
        print(name, "Invalid salary")
        continue

    if salary < 15000:
        increment = salary * 0.20
    elif salary <= 30000:
        increment = salary * 0.10
    else:
        increment = salary * 0.05

    new_salary = salary + increment
    updated_salaries[name] = new_salary

    print(name, "Old salary:", salary)
    print("New salary:", new_salary)

print("\nUpdated salary dictionary:")
print(updated_salaries)

