import json
import os

# Contact Manager CLI Application
# Stores and manages contacts + saves/loads from a JSON file

DATA_FILE = "contacts.json"
contact_list = []


def display_menu():
    print("\nCONTACT MANAGER")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")


def save_contacts():
    # Save the contact_list to a JSON file
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(contact_list, file, indent=2)


def load_contacts():
    # Load existing contacts from JSON file (if it exists)
    global contact_list

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                contact_list = json.load(file)
        except json.JSONDecodeError:
            # If file is corrupted/empty, start fresh
            contact_list = []
    else:
        contact_list = []


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
    save_contacts()

    print("Contact saved successfully.")


def view_contacts():
    if len(contact_list) == 0:
        print("No contacts stored.")
    else:
        for i, entry in enumerate(contact_list, start=1):
            print(f"{i}. {entry['name']} | {entry['phone']} | {entry['email']}")


def main():
    # THIS is the key line that makes it remember between runs
    load_contacts()

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