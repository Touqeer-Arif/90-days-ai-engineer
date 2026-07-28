#Mini Project 1 – Contact Book

contacts = {
    "Michael" : "03453234234",
    "Jake"    : "03456434568",
    "Alex"    : "03456476894",
    "Mike"    : "03458348694",
    "John"    : "03485967490"
}

def add_contact():
    name = str(input("Enter the name:"))
    number = input("Enter the number:")
    contacts[name] = number
    print("Contact successfully saved.")
    print()
def view_contact():
    for key,value in contacts.items():
        print(f"{key} : {value}")
        print()
def update_contact():
    name = input("Enter the Name:")
    contact = input("Enter the contact Number:")
    contacts[name] = contact
    print("Contact successfully Updated.")
    print()
def delete_contact():
    del_name = input("Enter the name of the person you want to delete:")
    if del_name in contacts:
        del contacts[del_name]
        print("Contact successfully Deleted.")
        print()
    else:
        print("No such contact found.")
        print()
def search_contact():
    search_name = input("Enter the name:")
    if search_name in contacts:
        print(f"{search_name} : {contacts[search_name]}")
        print()
    else:
        print("The name does not exist in the contacts.")
        print()

while True:
    print("       Contact Book      ")
    print()
    print("1.Add Contact")
    print("2.View Contact")
    print("3.Search Contact")
    print("4.Update Contact")
    print("5.Delete Contact")
    print("6.Exit")
    print()

    choice = int(input("Enter your choice:"))
    print()
    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contact()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
         print("Thankyou for using Contact Book.")
         break
    else:
            print("Wrong Choice.")