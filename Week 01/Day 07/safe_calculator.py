#Mini Project 1 – Safe Calculator using custom module

import calculator

while True:
    print("      Safe  Calculator     ")
    print()
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    print()
    try:
        choice = int(input("Enter your Choice: "))
        if choice >= 6:
            print("Invalid Choice")
            continue
        elif choice == 5:
            print("Thankyou for your Safe Calculator.")
            break
    except ValueError:
        print("Enter a valid choice.") 
        print()
        continue
    try:
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the Second number:"))

    except ValueError:
        print("Enter an Integer.")
        print()
        continue
        
    if choice == 1:
        print(f"Addition : {calculator.add(num1,num2)}")
        print()
    elif choice == 2:
        print(f"Subtraction : {calculator.sub(num1,num2)}")
        print()
    elif choice == 3:
        print(f"Multiplication : {calculator.mul(num1,num2)}")
        print()
    elif choice == 4:
        try:
            print(calculator.div(num1, num2))
            print()
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            print()
    else:
        print("Invalid Choice.")
        print()