def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    
    with open("CRUD_info.txt", "a") as file:
        file.write(f"{name}, {number}\n")
    print("Contact added successfully.")

def view_all_contacts():
    with open("CRUD_info.txt", "r") as file:
        contacts = file.readlines()
    
    if not contacts:
        print("No contacts found.")
    else:
        print()
        print("*********************************************")
        print("Contacts:")
        for contact in contacts:
            print(contact.strip())  # Remove newline characters
        print("*********************************************")

def update_contact():
    old_name = input("Enter the name of the contact to update: ")
    new_name = input("Enter the new name: ")
    new_number = input("Enter the new number: ")
    
    with open("CRUD_info.txt", "r") as file:
        lines = file.readlines()
    
    found = False
    with open("CRUD_info.txt", "w") as file:
        for line in lines:
            if old_name in line:
                file.write(f"{new_name}, {new_number}\n")
                found = True
            else:
                file.write(line)
    
    if found:
        print("Contact updated successfully.")
    else:
        print(f"Contact with name '{old_name}' not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    
    with open("CRUD_info.txt", "r") as file:
        lines = file.readlines()
    
    found = False
    with open("CRUD_info.txt", "w") as file:
        for line in lines:
            if name not in line:
                file.write(line)
            else:
                found = True
    
    if found:
        print("Contact deleted successfully.")
    else:
        print(f"Contact with name '{name}' not found.")

def search_by_contact_number():
    number = input("Enter the contact number to search for: ")
    
    with open("CRUD_info.txt", "r") as file:
        contacts = file.readlines()
    
    found = False
    for contact in contacts:
        name, contact_number = contact.strip().split(", ")
        if contact_number == number:
            print(f"Contact Name: {name}, Contact Number: {contact_number}")
            found = True
    
    if not found:
        print(f"No contact with number '{number}' found.")

def search_by_contact_name():
    name = input("Enter the contact name to search for: ")
    
    with open("CRUD_info.txt", "r") as file:
        contacts = file.readlines()
    
    found = False
    for contact in contacts:
        contact_name, contact_number = contact.strip().split(", ")
        if contact_name == name:
            print(f"Contact Name: {contact_name}, Contact Number: {contact_number}")
            found = True
    
    if not found:
        print(f"No contact with name '{name}' found.")





while True:
    print()
    print("1. Add Contact")
    print("2. View ALL Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search By Contact Number")
    print("6. Search By Contact Name")
    print("7. Exit")


    choice  = input("Enter your choices  from 1 to 7 : ")

    if choice == '1':
            add_contact()
    elif choice == '2':
        view_all_contacts()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        search_by_contact_number()
    elif choice == '6':
        search_by_contact_name()
    elif choice == '7':
        print("You have exited from application")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-7).")