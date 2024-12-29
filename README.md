# Contact-List-Manager
This program is a Contact List Manager that allows users to manage a list of contacts stored in a file. Users can view all contacts, add new contacts, delete existing ones, and exit the program. The file is automatically created if it doesn't exist, and all updates are saved persistently.

# Contact List Manager

## Description
The **Contact List Manager** is a Python program that allows users to manage a list of contacts. The application enables users to view existing contacts, add new ones, delete specific contacts, and save all changes to a file. This ensures persistent storage of the contact list for future sessions.

## Features
- **View Contacts**: Display a list of all saved contacts, showing their names and phone numbers.
- **Add Contact**: Add a new contact by entering a name and phone number.
- **Delete Contact**: Remove a contact by entering their exact name.
- **Persistent Storage**: All changes are saved to a file specified by the user.

## How to Use
1. Run the program in a Python environment.
2. When prompted, enter the file name to store or retrieve contacts.
3. Choose an option from the menu:
   - `1`: View all saved contacts.
   - `2`: Add a new contact.
   - `3`: Delete an existing contact.
   - `4`: Exit the program.
4. Follow the prompts for each option.

## Example Interaction
```plaintext
Welcome to Contact List Manager!
Options:
1. View Contacts
2. Add Contact
3. Delete Contact
4. Exit

What is the file name?
contacts.txt
Choose an option (1-4):
1
No contacts found.

Choose an option (1-4):
2
Enter name: Alice
Enter phone number: 123-456-7890
Contact saved.

Choose an option (1-4):
1
Here are the current contacts (Name - Phone Number):
Alice - 123-456-7890

Choose an option (1-4):
4
Goodbye!
```

## Requirements
- Python 3.x

## Error Handling
- If the file does not exist, it will be created automatically.
- Invalid input (e.g., entering text when an integer is required) will be caught and prompt the user to try again.
- Errors in file operations (e.g., permission issues) will display an appropriate message without crashing the program.

## Author
Created by: Fradley Joseph

