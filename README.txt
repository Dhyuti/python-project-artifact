CONTACT MANAGER (CLI) - Python

Student Name: Dhyuti Patel
Module: Programming Foundations (MK4-DF-PF-A25)
Assignment: 2 (Programming Artefact + Demonstration)

Overview:
This is a command-line Contact Manager application coded in Python.
This program allows users to create, view, delete, and search contacts.
Contacts are stored in a JSON file, hence persisting data.

Target user:
- Anyone interested in using a command-line tool for basic contact management.

Key Features:
- Add Contact (Create)
- View Contacts (Read)
- Delete Contact (Delete)
- Search Contacts (Read/search)

Improvements Added:
- Data persistence using JSON file
- Input validation
- Error handling using try/except block
- User-friendly menu system
- Formatted output


Program Structure:

The program is structured into functions, which are used to organize the code and make it easier to read.

`display_menu()`
This function is used to display the main menu of the command-line interface.

`add_contact()`
This function is used to create a new contact after validating the input.

`view_contacts()`
This function is used to show all the stored contacts in memory.

`delete_contact()`
This function is used to delete a chosen contact based on the index.

`search_contacts()`
This function is used to search for contacts based on name, phone, and email.

`save_contacts()`
This function saves the data into the JSON file.

`load_contacts()`
This function loads data from the JSON file at the start of the program.

`main()`
This is the main function, which controls the loop.

Data Structures Used:

The application uses a list of dictionaries to store contacts.

python
[
  {
    "name": "Dhyuti",
    "phone": "07411537502",
    "email": "Dhyuti.patel.338@cranfield.ac.uk"
  }
]

Reasons why this data structure was chosen

- Lists can be used to store many contacts
- Dictionaries can be used to store name, phone, and email information in a clear and easy-to-read format
- It can easily be converted to a JSON formating to be saved to a file

Validation Rules:

Name:
- Name should not be empty
- Name should only have letters, spaces, hyphens, and apostrophes

Phone:
- Phone should not be empty
- Phone should only have digits
- Phone should have 10-11 digits

Email:
- Email should not be empty
- Email should have '@'
- Email should have '.' after '@'


Files Included:

- main.py
  Main program file.

- contacts.json
  Stores data. Automatically updated when new contacts are added or existing ones are removed.

- git_log.txt
  Copy of commit log for proof of version control use.

- README.txt
  Instructions on running the program and explanation.


How to Run :

Option A (PyCharm):
1. Open the project folder in PyCharm
2. Open main.py
3. Click Run

Option B (Command Line / Terminal):
1. Open terminal in the project folder
2. Run:
   python main.py


Libraries Used:

- json (built-in): for saving and loading contacts from a JSON file
- os (built-in): for checking if the data file exists before loading

No external libraries are required.


Example Usage (Quick Demo):

1) Add Contact
- Select option 1
- Enter name, phone, and/or email
- The contact will be saved to contacts.json

2) Search
- Select option 4
- Enter a part of the name, phone, and/or email (e.g. "nat" or "@gmail")

3) Persistence check
- Exit the program
- Run the program again
- Select option 3 to view contacts and confirm they have been loaded

AI Usage:

I used AI tools during the development process for guidance and troubleshooting, particularly in the following areas:
- Code structuring in functions
- JSON save/load approach
- Basic ideas for input validation

I have reviewed and tested the suggestions and modified the code as follows:
- Changing the names and wording in the code and menu
- Adding more validation rules (e.g., phone length, name character limit)
- Adding search functionality and formatted outputs
- Test cases for empty inputs, invalid delete index, and invalid types

I am familiar and can explain all code in main.py.


Known Issues / Limitations:

- The code for validating emails is very basic and does not check all valid email addresses.
- The code for validating phone numbers assumes 10-11 digits and only digits, typical for UK phone numbers.

Testing:

The program has been manually tested using the following scenarios:

Test 1 - Add valid contact
Input: Valid data for name, phone, and email
Expected Output: The contact is added successfully.
Test 2 - Empty Name
Input: Empty data in the name field
Expected Output: The program prompts the user to enter a valid name.
Test 3 - Invalid Phone
Input: Contains letters or has a wrong number of digits
Expected Output: The program rejects the data.
Test 4 - Invalid Email
Input: Does not contain "@" and "."
Expected Output: The program rejects the data.
Test 5 - Delete contact
Input: Contains valid index number for the contact
Expected Output: The contact is deleted successfully.
Test 6 - Search functionality
Input: Partial data in the name and/or email field
Expected Output: The program displays the matching contacts.

Possible Future Improvements:

- Update contact feature (Edit)
- Export contacts to CSV
- Improve validation rules and test cases