# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 23:45:45 2024

@author: Fradley Joseph
"""
import sys
print("Welcome to Contact List Manager!\nOptions:\n1. View Contacts\n2. Add Contact\n3. Delete Contact\n4. Exit")

file = input("What is the file name?\n")

# Ensure the file exists
try:
    open(file, 'a').close()  # Create the file if it doesn't exist
except Exception as e:
    print(f"Error creating file: {e}")
    sys.exit()

def view_contacts(filename):
    """Display all contacts."""
    try:
        with open(filename, 'r') as f:
            data = f.readlines()
        if not data:
            print("No contacts found.")
        else:
            print("Here are the current contacts (Name - Phone Number):")
            for line in data:
                print(line.strip())
    except Exception as e:
        print(f"Error reading file: {e}")

def add_contacts(filename):
    """Add a new contact."""
    name = input('Enter name: ')
    phone = input('Enter phone number: ')
    contact = f"{name} - {phone}"
    try:
        with open(filename, 'a') as f:
            f.write(contact + '\n')
        print("Contact saved.")
    except Exception as e:
        print(f"Error saving contact: {e}")

def delete_contacts(filename):
    """Delete a contact by name."""
    name_to_delete = input("Enter the name of the contact to delete (exact match): ")
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        found = False
        with open(filename, 'w') as f:
            for line in lines:
                if name_to_delete not in line.split(' - ')[0].strip():
                    f.write(line)
                else:
                    found = True
        if found:
            print("Contact deleted.")
        else:
            print("Contact not found.")
    except Exception as e:
        print(f"Error deleting contact: {e}")

def option(x, filename):
    """Perform an action based on user choice."""
    if x == 1:
        view_contacts(filename)
    elif x == 2:
        add_contacts(filename)
    elif x == 3:
        delete_contacts(filename)
    elif x == 4:
        print("Goodbye!")
        sys.exit()
    else:
        print("Not a valid option. Please try again (1-4).\n")

# Main Loop
while True:
    try:
        user_input = int(input('Choose an option (1-4): \n'))
        option(user_input, file)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
