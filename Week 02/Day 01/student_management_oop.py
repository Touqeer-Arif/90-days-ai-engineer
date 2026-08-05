"""Create:

class Student

Methods:

Add Student
Display Student
Update Student
Delete Student

Store students in a list.
"""
students = []

class Student:

    def add_student(self):
        name = input("Enter the student Name:")
        roll_no = input("Enter the Roll Number:")
        course = input("Enter the Course:")

        student = {
            "Name" : name,
            "Roll Number" : roll_no,
            "Course" : course
        }

        students.append(student)
        print("Student Added Successfully!")
        print()

    def display_student(self):
        if not students:
            print("No student Found.\n")
            return
        for i in students:
            print("   Students  List   \n ")
            print(f"Name : {i['Name']}")
            print(f"Roll Number : {i["Roll Number"]}")
            print(f"Course : {i["Course"]}")
            print()

    def update_student(self):
        roll_no = input("Enter the Roll Number:\n")

        for i in students:
            if i["Roll Number"] == roll_no:
                i["Name"] = input("Enter the New Name:")
                i["Course"] = input("Enter the New Course:")
                print("Student Updated Sucessfully!\n")
                return
        print("Student not found.\n")

    def delete_student(self):
        roll_no = input("Enter the Roll Number:")
        for i in students:
            if i["Roll Number"] == roll_no:
                students.remove(i)
                print("Student Deleted Successfully.\n")
                return 
        print("Student Not Found.\n")

obj = Student()

while True:
    print(" Student  Management  System  \n")
    print("1.Add Student")
    print("2.Display Student")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Exit\n")

    choice = int(input("Enter your choice:\n"))
    print()
    if choice == 1:
        obj.add_student()
    elif choice == 2:
        obj.display_student()
    elif choice == 3:
        obj.update_student()
    elif choice == 4:
        obj.delete_student()
    elif choice == 5:
        print("Thanks for using")
        break
    else:
        print("Invalid Choice.")
    
            
            