users = ["admin", "prathamesh", "tester"]

def add_user(username):

    if username in users:
        print("User already exists")

    else:
        users.append(username)
        print("User created successfully")


def delete_user(username):

    if username in users:
        users.remove(username)
        print("User deleted successfully")

    else:
        print("User not found")


def show_users():

    print("\nLinux Users:")

    for user in users:
        print(user)


add_user("cloud developer")
delete_user("tester")
show_users()