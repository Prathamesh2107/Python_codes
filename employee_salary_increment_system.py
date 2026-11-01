employees = {
    "Amit": 15000,
    "Rahul": 35000,
    "Priya": 55000,
    "Sneha": -28000,
    "Raj": 4500
}

updated_salaries = {}

for name, salary in employees.items():
    if salary <= 0:
        print(name, "Invalid salary")
        continue

    if salary < 25000:
        increment = salary * 0.20
    elif salary <= 50000:
        increment = salary * 0.10
    else:
        increment = salary * 0.05

    new_salary = salary + increment
    updated_salaries[name] = new_salary

    print(name, "Old salary:", salary)
    print("New salary:", new_salary)

print("\nUpdated salary dictionary:")
print(updated_salaries)

