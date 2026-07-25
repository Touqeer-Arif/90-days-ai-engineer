#Mini Project 1 – Number Guessing Game

"""
Requirements:

Computer chooses a random number between 1 and 100.
User keeps guessing.
Tell the user:
Too High
Too Low
Correct!
Count the number of attempts.
Ask if the user wants to play again.

"""

import random 

while True:
    number = random.randint(1,100)
    attempts = 0
    
    print("   Number Guessing Game   ")
    print("Guess a Number between 1 and 100")
    
    while True:
        guess = int(input("Enter the guess Number:"))
        attempts += 1
        if guess < number:
            print("Too Low")
        elif guess > number:
            print("Too High")
        elif guess == number:
            print("Correct!")
            print(f"The number of attempts to guess  the number:{attempts}")
            break
            
    again = str(input("Do you want to play again?(yes/no):")).lower()
    if again == "no":
            print("Thanks for Playing!")
            break