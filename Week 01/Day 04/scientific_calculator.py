#Mini Project 1 – Scientific Calculator

"""
Create:
scientific_calculator

Requirements:

Functions:
Addition
Subtraction
Multiplication
Division
Power
Square Root
Modulus

Menu:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
7. Modulus
8. Exit

Each operation must be implemented as a separate function.

"""

import math

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def divide(a,b):
    return a / b
def multiply(a,b):
    return a * b
def modulus(a,b):
    return a % b
def square_root(a):
    return math.sqrt(a)
def power(a,b):
    return a**b


print("    Scientific Calculator     ")
print()
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
print("6.Square Root")
print("7.Power")
print("8.Exit")
print()

while True:
    choice = int(input("Enter your choice:"))
    if choice == 6:
        num = int(input("Enter the number: "))
        if num < 0:
            print("Error: Cannot find the square root of a negative number.")
        else:
            print(f"The result is : {square_root(num)}")
            print()
    elif choice == 8:
        print("Thankyou for using Scientific Calculator.")
        break
    else:
        number1 = int(input("Enter the first number:"))
        number2 = int(input("Enter the second number:"))

        if choice == 1:
            print(f"The result after Addition is : {add(number1,number2)}")
            print()
        elif choice == 2:
            print(f"The result after Subtraction is : {subtract(number1,number2)}")
            print()
        elif choice == 3:
            print(f"The result after Multiplication is : {multiply(number1,number2)}")
            print()
        elif choice == 4:
            if number2 == 0:
                print("Error: Cannot divide by zero.")
                print()
            else:
                print(f"The result after Division is : {divide(number1, number2)}")
                print()
        elif choice == 5:
            if number2 == 0:
                print("Error: Cannot perform modulus by zero.")
                print()
            else:
                print(f"The result after Modulus is : {modulus(number1, number2)}")
                print()
        elif choice == 7:
            print(f"The result after Power is : {power(number1,number2)}")
            print()
        else:
            print("Invalid Choice")