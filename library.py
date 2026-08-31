import json
import os

FILE_NAME = "books.json"


def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return []


def save_books(books):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def add_book():
    books = load_books()

    title = input("Book title: ")
    author = input("Author: ")
    status = input("Status (reading/finished): ")

    book = {
        "title": title,
        "author": author,
        "status": status
    }

    books.append(book)
    save_books(books)

    print("Book added successfully.")


def view_books():
    books = load_books()

    if len(books) == 0:
        print("No books found.")
        return

    for index, book in enumerate(books, start=1):
        print(index, book["title"], book["author"], book["status"])

def search_book():
    books = load_books()

    keyword = input("Search keyword: ")

    found = False

    for index, book in enumerate(books, start=1):
        if keyword.lower() in book["title"].lower():
            print(index, book["title"], book["author"], book["status"])
            found = True

    if found == False:
        print("No matching books found.")

def update_status():
    books = load_books()

    if len(books) == 0:
        print("No books found.")
        return

    view_books()

    book_number = int(input("Enter book number to update: "))
    new_status = input("New status (reading/finished): ")

    if book_number < 1 or book_number > len(books):
        print("Invalid book number.")
        return

    books[book_number - 1]["status"] = new_status
    save_books(books)

    print("Book status updated successfully.")

def edit_book():
    books = load_books()

    if len(books) == 0:
        print("No books found.")
        return

    view_books()

    book_number = int(input("Enter book number to edit: "))

    if book_number < 1 or book_number > len(books):
        print("Invalid book number.")
        return

    book = books[book_number - 1]

    new_title = input("New title: ")
    new_author = input("New author: ")
    new_status = input("New status (reading/finished): ")

    book["title"] = new_title
    book["author"] = new_author
    book["status"] = new_status

    save_books(books)

    print("Book updated successfully.")

def delete_book():
    books = load_books()

    if len(books) == 0:
        print("No books found.")
        return

    view_books()

    book_number = int(input("Enter book number to delete: "))

    if book_number < 1 or book_number > len(books):
        print("Invalid book number.")
        return

    deleted_book = books.pop(book_number - 1)
    save_books(books)

    print("Deleted book:", deleted_book["title"])

def show_statistics():
    books = load_books()

    total_count = len(books)
    reading_count = 0
    finished_count = 0

    for book in books:
        if book["status"] == "reading":
            reading_count = reading_count + 1
        elif book["status"] == "finished":
            finished_count = finished_count + 1

    print("\nLibrary Statistics")
    print("Total books:", total_count)
    print("Reading:", reading_count)
    print("Finished:", finished_count)

def main():
    while True:
         print("1. Add book")
         print("2. View books")
         print("3. Search book")
         print("4. Update status")
         print("5. Edit book")
         print("6. Delete book")
         print("7. Show statistics")
         print("8. Exit")

         choice = input("Choose an option: ")

         if choice == "1":
              add_book()
         elif choice == "2":
              view_books()
         elif choice == "3":
              search_book()
         elif choice == "4":
              update_status()
         elif choice == "5":
              edit_book()
         elif choice == "6":
              delete_book()
         elif choice == "7":
               show_statistics()
         elif choice == "8":
               print("Goodbye.")
               break
         else:
               print("Invalid option.")
main()