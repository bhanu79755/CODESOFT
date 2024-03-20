class Contact:
    def _init_(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def _init_(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for i, contact in enumerate(self.contacts):
            print(f"{i+1}. {contact.name} - {contact.phone_number} - {contact.email} - {contact.address}")

    def update_contact(self, index, **kwargs):
        if index-1 < len(self.contacts):
            for key, value in kwargs.items():
                setattr(self.contacts[index-1], key, value)

    def delete_contact(self, index):
        del self.contacts[index-1]

if __name__ == "__main__":
    contact_book = ContactBook()
    while True:
        action = input("What would you like to do? (add/display/update/delete/quit)\n")
        if action == "add":
            contact_book.add_contact(Contact(*input("Enter the name, phone number, email and address separated by comma:\n").split(',')))
        elif action == "display":
            contact_book.display_contacts()
        elif action == "update":
            index = int(input("Which contact would you like to update?"))
            contact_book.update_contact(index, **dict((k.strip(), v.strip()) for k,v in (x.split('=') for x in input("Enter key-value pairs seperated by commas:\n").split(','))))
        elif action == "delete":
            contact_book.delete_contact(int(input("Which contact would you like to delete?")))
        elif action == "quit":
            break
        else:
            print("Invalid command.")