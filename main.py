# Contact Manager CLI Application
# Stores and manages contacts in memory

contact_list = []


def display_menu():
    print("\nCONTACT MANAGER")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    entry = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contact_list.append(entry)

    print("Contact saved successfully.")


def view_contacts():
    if len(contact_list) == 0:
        print("No contacts stored.")
    else:
        for entry in contact_list:
            print(entry)


def main():
    menu_choice = ""

    while menu_choice != "3":
        display_menu()

        menu_choice = input("Enter choice: ")

        if menu_choice == "1":
            add_contact()

        elif menu_choice == "2":
            view_contacts()

        elif menu_choice == "3":
            print("Have a nice day :)")

        else:
            print("Try again, invalid input!")


if __name__ == "__main__":
    main()