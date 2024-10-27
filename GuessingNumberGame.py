import random

Random_Number = random.randint(1,100)
Guessed_Number = int(input("Guess a number between 1 to 100: "))
No_of_Guesses = 0

while Random_Number != Guessed_Number:
    if Guessed_Number > Random_Number:
        Guessed_Number = int(input("Guess another number, your guess is too high: "))
    else:
        Guessed_Number = int(input("Guess another number, your guess is too low: "))
    No_of_Guesses += 1

print("You guess the number! it took you ", No_of_Guesses, " of guesses!")