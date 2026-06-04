contacts = []

def add_contact():
    print("\nADD CONTACT")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    print("\nCONTACT LIST")

    if not contacts:
        print("No contacts available.")
        return

    print("-" * 60)
    print("{:<20} {:<15}".format("Name", "Phone Number"))
    print("-" * 60)

    for contact in contacts:
        print("{:<20} {:<15}".format(
            contact["name"],
            contact["phone"]
        ))

def search_contact():
    search = input("\nEnter Name or Phone Number to Search: ")

    found = False

    for contact in contacts:
        if search.lower() == contact["name"].lower() or search == contact["phone"]:
            print("\nCONTACT FOUND")
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    phone = input("\nEnter Phone Number of Contact to Update: ")

    for contact in contacts:
        if contact["phone"] == phone:
            print("Enter New Details")

            contact["name"] = input("New Name: ")
            contact["phone"] = input("New Phone Number: ")
            contact["email"] = input("New Email: ")
            contact["address"] = input("New Address: ")

            print("Contact updated successfully.")
            return

    print("Contact not found.")

def delete_contact():
    phone = input("\nEnter Phone Number of Contact to Delete: ")

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return

    print("Contact not found.")

while True:
    print("\n" + "=" * 50)
    print("CONTACT BOOK MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Book.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")