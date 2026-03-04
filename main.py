import json
import os

# Contact Manager CLI Application
# Stores and manages contacts + saves/loads from a JSON file
# AI USAGE NOTE:
# I used AI for guidance on structuring the program into functions and handling JSON save/load.
# I then added validation rules,renamed variables, added search functionality and tested edge cases myself.

Contacts_File = "contacts.json"
contact_list = []


def display_menu():
    print("\nCONTACTS")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Search Contacts")
    print("5. Exit")


def save_contacts():
    # Save the contact_list to a JSON file
    with open(Contacts_File, "w", encoding="utf-8") as file:
        json.dump(contact_list, file, indent=2)


def load_contacts():
    # Load existing contacts from JSON file (if it exists)
    global contact_list

    if os.path.exists(Contacts_File):
        try:
            with open(Contacts_File, "r", encoding="utf-8") as file:
                contact_list = json.load(file)
        except json.JSONDecodeError:
            contact_list = []
    else:
        contact_list = []

def get_valid_name():
    while True:
        name = input("Enter contact name: ").strip()

        if name == "":
            print("Name cannot be empty.")
            continue

        allowed_chars = set(" -'")
        if all(char.isalpha() or char in allowed_chars for char in name):
            return name

        print("Name must contain only letters (spaces, - and ' allowed).")

def get_valid_email():
    while True:
        email = input("Enter email address: ").strip()

        if email == "":
            print("Email cannot be empty.")
            continue

        if "@" in email:
            parts = email.split("@")
            if len(parts) == 2 and parts[0] != "" and parts[1] != "" and "." in parts[1]:
                return email

        print("Email must contain an '@' and a '.' after the '@' (e.g. name@example.com).")

def get_valid_phone():
    while True:
        phone = input("Enter phone number: ").strip()

        if phone == "":
            print("Phone number cannot be empty.")
            continue

        if phone.isdigit() and 10 <= len(phone) <= 11:
            return phone

        print("Phone number must contain only digits and be 10–11 numbers long.")



def add_contact():
    name = get_valid_name()
    phone = get_valid_phone()
    email = get_valid_email()

    user_input = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contact_list.append(user_input)
    save_contacts()

    print("Contact saved successfully.")


def view_contacts():
    if len(contact_list) == 0:
        print("No contacts stored.")
    else:
        for i, User_Input in enumerate(contact_list, start=1):
            print(f"{i}. {User_Input['name']} | {User_Input['phone']} | {User_Input['email']}")


def delete_contact():
    view_contacts()

    if len(contact_list) == 0:
        return

    try:
        index = int(input("Enter number of contact to delete: ")) - 1

        if 0 <= index < len(contact_list):
            removed = contact_list.pop(index)
            save_contacts()
            print(f"{removed['name']} deleted successfully.")
        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")


def search_contacts():
    if len(contact_list) == 0:
        print("No contacts stored.")
        return

    keyword = input("Search by name, phone, or email: ").lower().strip()

    results = []

    for User_Input in contact_list:
        if (keyword in User_Input["name"].lower() or
            keyword in User_Input["phone"] or
            keyword in User_Input["email"].lower()):
            results.append(User_Input)

    if len(results) == 0:
        print("No matching contacts found.")
    else:
        print("\nSearch Results:")
        for i, User_Input in enumerate(results, start=1):
            print(f"{i}. {User_Input['name']} | {User_Input['phone']} | {User_Input['email']}")


def main():
    load_contacts()

    menu_choice = ""

    while menu_choice != "5":
        display_menu()
        menu_choice = input("Enter choice: ")

        if menu_choice == "1":
            add_contact()
        elif menu_choice == "2":
            view_contacts()
        elif menu_choice == "3":
            delete_contact()
        elif menu_choice == "4":
            search_contacts()
        elif menu_choice == "5":
            print("Have a nice day :)")
        else:
            print("Try again, invalid input!")


if __name__ == "__main__":
    main()