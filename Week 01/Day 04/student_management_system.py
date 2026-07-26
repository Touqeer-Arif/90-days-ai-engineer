#Mini Project 2 – Student Management System (Functions Version)

"""

Create:
student_management_system

Menu:
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit

Each option must call a separate function.

Store student data in a list for now.

"""

students = ["Harry","Jack","Joe","Machane"]

def add_student():
    name = str(input("Enter the student name:"))
    students.append(name)
    print("Student Added Successfully.")
    print()
def view_student():
    if len(students) == 0:
        print("No Student Found.")
        print()
    else:
        print("Student's List:")
        for student in students:
            print(student)
        print()
def search_student():
    name = str(input("Enter the name of the Student:"))
    if name in students:
        print("Student Found")
        print()
    else:
        print("Student Not Found.")
        print()
def delete_student():
    name = str(input("Enter the name of the Student:"))
    if name in students:
        students.remove(name)
        print("Student Removed Successfully")
        print()
    else:
        print("No Student Found.")
        print()

print("       Student Management System    ")
print()
print("1.Add Student")
print("2.View Student")
print("3.Search Student")
print("4.Delete Student")
print("5.Exit")
print()

while True:
    choice = int(input("Enter your Choice:"))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        print("Thankyou for using the Student Management System.")
        break
    else:
        print("Invalid Choice.")