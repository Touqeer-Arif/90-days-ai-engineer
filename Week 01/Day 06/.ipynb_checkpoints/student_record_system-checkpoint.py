# Mini Project 2 – Student Record System

def add_student():
    name = input("Enter the name of the student:")
    roll_no = input("Enter the Roll no of the student:")
    cgpa = input("Enter the CGPA of the student:")
    with open ("students.txt","a") as file:
        file.write(f"\nname : {name} , Roll No : {roll_no} , CGPA : {cgpa}")
        print()

def view_student():
    with open ("students.txt","r") as file:
        data = file.read()
        if data.strip():
            print("\n   Student's  List    ")
            print(data)
            print()
        else:
            print("No Students enlisted.")
            print()

def search_student():
    word = input("Enter the name of the student you want to search:")
    with open ("students.txt","r") as file:
        data = file.readlines()
    found = False
    print("Matching Students:")
    for line in data:
        if word.lower() in line.lower():
            print(line.strip())
            found = True
            print()
    if not found:
        print("No such Student found in the file.")
        print()

while True:
    print("\n      Student Record System     ")
    print()
    print("1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Exit")
    print()

    choice = int(input("Enter your choice:"))
    print()
    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        print("Thanks for using Student Record System.")
        break
    else:
        print("Wrong Choice")