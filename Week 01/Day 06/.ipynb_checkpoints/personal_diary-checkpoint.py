# Mini Project 1 – Personal Diary

def add_entry():
    entry = input("Write what you want to add into your diary:")
    with open ("diary.txt","a") as file:
        file.write(f"\n{entry}")
        print()

def view_all():
    with open ("diary.txt","r") as file:
        data = file.read()
        if data.strip():
            print("\n--- Diary Entries ---")
            print(data)
            print()
        else:
            print("No diary entries found.")
            print()

def search_word():
    word = input("Enter the word you want to search:")
    with open ("diary.txt","r") as file:
        data = file.readlines()
    found = False
    print("Matching Entries:")
    for line in data:
        if word.lower() in line.lower():
            print(line.strip())
            found = True
            print()
    if not found:
        print("No such word found in the file:")
        print()

while True:
    print("      Personal Diary      ")
    print()
    print("1.Write a Diary Entry")
    print("2.View all entries")
    print("3.Searh for a Word")
    print("4.Exit")
    print()

    choice = int(input("Enter your choice:"))
    print()
    if choice == 1:
        add_entry()
    elif choice == 2:
        view_all()
    elif choice == 3:
        search_word()
    elif choice == 4:
        print("Thanks for using Personal Diary.")
        break
    else:
        print("Wrong Choice")