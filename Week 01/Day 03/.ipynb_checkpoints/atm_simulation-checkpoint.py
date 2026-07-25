#Mini Project 2 – ATM Simulation

"""
Requirements:

Starting balance: 5000
Deposit updates the balance.
Withdraw only if sufficient balance exists.
Repeat until the user chooses Exit.

"""

balance = 5000

while True:
    print("    ATM    ")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")

    choice = int(input("Enter what you want to do:"))
    if choice == 1:
        print(f"Your current balance is: {balance}")
    elif choice == 2:
        amt = int(input("Enter the amount to Deposit:"))
        balance += amt
        print(f"Your Current balance is: {balance}")
    elif choice == 3:
        amtt = int(input("Enter the amount to Withdraw:"))
        if amtt > balance:
            print("Insufficient Balance")
        elif amt <= balance:
            balance -= amtt
            print(f"Your current balance is: {balance}")
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Invalid choice")