from lib.helpers import exit_program
from lib.controllers.user_controller import create_user, list_users
from lib.controllers.book_controller import add_book, list_books
from lib.controllers.reading_status_controller import add_status, view_user_statuses

def menu():
    print("\nBook Tracker CLI")
    print("1. Create User")
    print("2. List Users")
    print("3. Add Book")
    print("4. List Books")
    print("5. Add Reading Status")
    print("6. View User Reading Statuses")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            name = input("Enter user name: ")
            create_user(name)
        elif choice == "2":
            list_users()
        elif choice == "3":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            add_book(title, author)
        elif choice == "4":
            list_books()
        elif choice == "5":
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            status = input("Enter reading status (Reading/Completed): ")
            add_status(user_id, book_id, status)
        elif choice == "6":
            user_id = int(input("Enter user ID: "))
            view_user_statuses(user_id)
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
