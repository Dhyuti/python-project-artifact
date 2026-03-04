# Contact Manager CLI Application
# This program allows a user to store and manage contacts.

def display_menu():
    print("\nCONTACT MANAGER")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")


def main():
    choice = ""

    while choice != "3":
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            print("Add contact feature coming soon")
        elif choice == "2":
            print("View contacts feature coming soon")
        elif choice == "3":
            print("Have a nice day!")
        else:
            print("Try again, invalid input")


if __name__ == "__main__":
    main()