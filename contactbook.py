import sys

contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nContact List:")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    query = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if name.lower() == contact['name'].lower():
            print("Leave blank to keep current value.")
            new_name = input(f"New Name [{contact['name']}]: ") or contact['name']
            new_phone = input(f"New Phone [{contact['phone']}]: ") or contact['phone']
            new_email = input(f"New Email [{contact['email']}]: ") or contact['email']
            new_address = input(f"New Address [{contact['address']}]: ") or contact['address']
            contact.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            })
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if name.lower() == contact['name'].lower():
            del contacts[i]
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def main():
    while True:
        print("Contact Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()