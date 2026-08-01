#Mini Project 2 – Student Result Analyzer

import calculator

lists = []
total = []

while True:
    print("      Student Result Analyzer     ")
    print()
    try:
        subjects = int(input("Enter the total number of subjects:"))
        if subjects <= 0:
            print("Number of Subjects must be greater than 0.")
            print()
            continue
        break 
    except ValueError:
        print("Enter a Valid Number.")
        print()
    
for i in range(subjects):
    
    while True:
        try:
            obt_mark = int(input(f"Enter the obtained marks for subject {i+1} : "))
            if obt_mark < 0:
                print("Number Cannot be Negative.")
                print()
                continue
            break
        except ValueError:
            print("Enter a Valid Number.")
            
    while True:
        try:
            total_mark = int(input(f"Enter the total marks for subject {i+1} : "))
            if total_mark < 0:
                print("Number Cannot be Negative.")
                print()
                continue
            break
        except ValueError:
            print("Enter Valid Number.")
    lists.append(obt_mark)
    total.append(total_mark)
    print()

sum_marks = sum(lists)
num_subj = len(total)
max_marks = max(lists)
min_marks = min(lists)

while True:
    print()
    print("1.Average")
    print("2.Highest")
    print("3.Lowest")
    print("4.Exit")
    print()

    try:
        choice = int(input("Enter your Choice: "))
        if choice >= 5:
            print("Invalid Choice")
            continue
        elif choice == 4:
            print("Thankyou for your Safe Calculator.")
            break
    except ValueError:
        print("Enter a valid choice.") 
        print()
        continue

    if choice == 1:
        print(f"Average : {calculator.average(sum_marks,num_subj)}")
        print()
    elif choice == 2:
        print(f"Maximum Marks : {max_marks}")
        print()
    elif choice == 3:
        print(f"Minimum Marks : {min_marks}")
        print()
    else:
        print("Invalid Choice.")
        print()