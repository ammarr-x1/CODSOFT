
class Contacts:
    def __init__(self,name,num,email,add):
        self.name = name
        self.number = num
        self.email = email
        self.address = add

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self,name,num,email,add):
        contact = Contacts(name,num,email,add)
        self.contacts.append(contact)

    def view_contact(self):
        if self.contacts:
            print("**** Contacts ****")
            for i,contact in enumerate(self.contacts,start=1):
                print(f"Name : {contact.name} \tNumber : {contact.number}\temail : {contact.email} \tAddress : {contact.address}")
        else:
            print("No Contacts Found")

    def search_contact(self,query):
        found_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() :
                found_contacts.append(contact)

        if not found_contacts:
            print("No contacts Found")
        else:
            for i,contact in enumerate(found_contacts,start=1):
                print(f"{i}.Name : {contact.name} Number : {contact.number} email : {contact.email} Address : {contact.address} ")

    def update_contact(self,index,name,num,email,add):
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            contact.name = name
            contact.number = num
            contact.email = email
            contact.address = add
            print("Contact Updated")
        else:
            print("Invalid Index Number")

    def del_contact(self,index):
        if 0 <= index <len(self.contacts):
            del self.contacts[index]
        else:
            print("Invalid Index Number")

def main():
    contacts = PhoneBook()

    while True:
        print("---> PHONE BOOK <---")
        print("1.Add Contact")
        print("2.View Contact")
        print("3.Search Contact")
        print("4.Update Contact")
        print("5.Delete Contact")
        print("6.Exit")

        try:
            choice = int(input("Enter Your Choice\n"))

            if choice == 1:
                name = input("Enter Name:")
                num = int(input("Enter Phone Number:"))
                email = input("Enter Email:")
                add = input("Enter Address:")

                contacts.add_contact(name, num, email, add)

            elif choice == 2:
                contacts.view_contact()

            elif choice == 3:
                query = input("Enter Name to search: ")
                contacts.search_contact(query)

            elif choice == 4:
                contacts.view_contact()
                index = int(input("Enter The Number of contact to be updated :")) - 1
                name = input("Enter Name:")
                num = int(input("Enter Phone Number:"))
                email = input("Enter Email:")
                add = input("Enter Address:")
                contacts.update_contact(index, name, num, email, add)

            elif choice == 5:
                contacts.view_contact()
                index = int(input("Enter the number of contact to be deleted :")) - 1
                contacts.del_contact(index)

            elif choice == 6:
                print("GoodBye")
                break

            else:
                print("Invalid Choice")
        except ValueError:
            print("Invalid 1212")

if __name__ == '__main__':
    main()

