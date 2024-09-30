class ContactMaster:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {
            'Name': name,
            'Phone': phone,
            'Email': email
        }
        self.contacts.append(contact)
        print(f"Contact '{name}' has been added successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\n--- Contact List ---")
            for idx, contact in enumerate(self.contacts, 1):
                print(f"{idx}. {contact['Name']}")
                print(f"   Phone: {contact['Phone']}")
                print(f"   Email: {contact['Email']}")

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if name.lower() in contact['Name'].lower()]
        if found_contacts:
            for contact in found_contacts:
                print(f"Name: {contact['Name']}")
                print(f"Phone: {contact['Phone']}")
                print(f"Email: {contact['Email']}")
        else:
            print(f"No contacts found with the name '{name}'.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['Name'].lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' has been deleted.")
                return
        print(f"No contact found with the name '{name}'.")

def menu():
    contact_manager = ContactMaster()
    
    while True:
        print("\n--- ContactMaster Menu ---")
        print("1. Add New Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, phone, email)

        elif choice == '2':
            contact_manager.display_contacts()

        elif choice == '3':
            name = input("Enter the name to search: ")
            contact_manager.search_contact(name)

        elif choice == '4':
            name = input("Enter the name to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '5':
            print("Exiting ContactMaster. Goodbye!")
            break

        else:
            print("Invalid choice, please select an option between 1 and 5.")


if __name__ == "__main__":
    menu()
