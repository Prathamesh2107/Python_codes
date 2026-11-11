def calculate_storage(used, total):

    try:

        percentage = (used / total) * 100

        print("Storage Used:", percentage, "%")

    except ZeroDivisionError:
        print("Error: Total storage cannot be zero")

    except TypeError:
        print("Error: Please enter numeric values")


calculate_storage(800, 1000)
calculate_storage(500, 0)