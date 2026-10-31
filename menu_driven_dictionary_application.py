students = {"Pratham":90,
            "Rohit":84,
            "Virat":98,
            "Varad":85,
            "Sakshi":67}
while True:
    print("\n--- Student Management ---")
    print("1. Add student")
    print("2. Search student")
    print("3. Update marks")
    print("4. Delete student")
    print("5. Display all students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        if name in students:
            print("Student already exists")
        else:
            try:
                marks = float(input("Enter marks: "))

                if 0 <= marks <= 100:
                    students[name] = marks
                    print("Student added successfully")
                else:
                    print("Marks must be between 0 and 100")

            except ValueError:
                print("Enter valid numeric marks")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found")

    elif choice == "3":
        name = input("Enter student name: ")

        if name in students:
            try:
                marks = float(input("Enter new marks: "))

                if 0 <= marks <= 100:
                    students[name] = marks
                    print("Marks updated")
                else:
                    print("Marks must be between 0 and 100")

            except ValueError:
                print("Enter valid numeric marks")
        else:
            print("Student not found")

    elif choice == "4":
        name = input("Enter student name: ")

        if name in students:
            del students[name]
            print("Student deleted")
        else:
            print("Student not found")

    elif choice == "5":
        if students:
            for name, marks in students.items():
                print(name, ":", marks)
        else:
            print("No student records available")

    elif choice == "6":
        print("Program exited")
        break

    else:
        print("Invalid choice")

