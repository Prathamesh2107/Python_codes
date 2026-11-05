library = {
    "Python": {
        "total": 5,
        "available": 5
    },
    "AWS": {
        "total": 3,
        "available": 3
    },
    "Linux": {
        "total": 4,
        "available": 4
    }
}

issued_books = {}

def issue_book(book, student):

    if book not in library:
        print("Book not found")

    elif library[book]["available"] <= 0:
        print("Book unavailable")

    else:
        library[book]["available"] -= 1

        issued_books[student] = book

        print("Book issued successfully")


def return_book(student):

    if student not in issued_books:
        print("No issued book found")

    else:
        book = issued_books[student]

        library[book]["available"] += 1

        del issued_books[student]

        print("Book returned successfully")


issue_book("Python", "Amit")
issue_book("Python", "Rahul")

return_book("Amit")

print("\nLibrary Inventory:", library)
print("Issued Books:", issued_books)