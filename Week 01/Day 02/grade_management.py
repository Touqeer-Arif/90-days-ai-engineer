#Mini Project:Student Grade Management System
"""Program Requirements:
Ask:
Student Name
Roll Number
Subject 1 Marks
Subject 2 Marks
Subject 3 Marks
Subject 4 Marks
Subject 5 Marks
Calculate:
Total Marks
Average
Percentage
Determine Grade"""

name = str(input("Enter Student Name:"))
roll_no = int(input("Enter the Roll Number:"))
subj_1 = int(input("Enter Subject 1 Obtained Marks:"))
subj_01 = int(input("Enter Subject 1 Total Marks:"))
subj_2 = int(input("Enter Subject 2 Obtained Marks:"))
subj_02 = int(input("Enter Subject 2 OTotal Marks:"))
subj_3 = int(input("Enter Subject 3 Obtained Marks:"))
subj_03 = int(input("Enter Subject 3 Total Marks:"))
subj_4 = int(input("Enter Subject 4 Obtained Marks:"))
subj_04 = int(input("Enter Subject 4 Total Marks:"))
subj_5 = int(input("Enter Subject 5 Obtained Marks:"))
subj_05 = int(input("Enter Subject 5 Total Marks:"))

obtained_marks = subj_1+subj_2+subj_3+subj_4+subj_5
total_marks = subj_01+subj_02+subj_03+subj_04+subj_05
average = obtained_marks/5
percentage = (obtained_marks/total_marks) * 100

if percentage >= 90 and percentage <= 100:
    print()
    print(f"Student Name   :{name}")
    print(f"Roll Number    :{roll_no}")
    print(f"Obtained Marks :{obtained_marks}")
    print(f"Total Marks    :{total_marks}")
    print(f"Average        :{average}")
    print(f"Grade          :A+")
    print("Congratulations!")
elif percentage >= 80 and percentage <= 89:
    print()
    print(f"Student Name   :{name}")
    print(f"Roll Number    :{roll_no}")    
    print(f"Obtained Marks :{obtained_marks}")
    print(f"Total Marks    :{total_marks}")
    print(f"Average        :{average}")
    print(f"Grade          :A")
    print("Keep Working Hard!")
elif percentage >= 70 and percentage <= 79:
    print()
    print(f"Student Name   :{name}")
    print(f"Roll Number    :{roll_no}")    
    print(f"Obtained Marks :{obtained_marks}")
    print(f"Total Marks    :{total_marks}")
    print(f"Average        :{average}")
    print(f"Grade          :B")
    print("Keep Working Hard!")
elif percentage >= 60 and percentage <= 69:
    print()
    print(f"Student Name   :{name}")
    print(f"Roll Number    :{roll_no}")    
    print(f"Obtained Marks :{obtained_marks}")
    print(f"Total Marks    :{total_marks}")
    print(f"Average        :{average}")
    print(f"Grade          :C")
    print("Keep Working Hard!")
elif percentage >= 50 and percentage <= 59:
    print()
    print(f"Student Name   :{name}")
    print(f"Roll Number    :{roll_no}")    
    print(f"Obtained Marks :{obtained_marks}")
    print(f"Total Marks    :{total_marks}")
    print(f"Average        :{average}")
    print(f"Grade          :D")
    print("Keep Working Hard!")
elif percentage >= 0 and percentage <= 49:
    print()
    print(f"Student Name   :{name}")
    print(f"Roll Number    :{roll_no}")    
    print(f"Obtained Marks :{obtained_marks}")
    print(f"Total Marks    :{total_marks}")
    print(f"Average        :{average}")
    print(f"Grade          :Fail")
    print("Keep Working Hard!")