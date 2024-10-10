#implort randm module
import random

#take names of both players and welcome them
player1 = input("Hey, What's your good name?")
print(f"Hi {player1}, Welcome to MasterMind Game!. You are Player1")
player2 = input("Hey, What's your good name?")
print(f"Hi {player2}, Welcome to MasterMind Game!. You are Player2")

#player1 sets a number for player2 to guess
no = int(input(f"{player1} enter a number between 1000 to 9999 for other player to guess: "))
while True:
    if no in range(1000, 10000):
        print(f"{player2} you have to guess the number in 10 attempts")
        break
    else:
        print("Invalid number, please enter a number between 1000 to 9999")
        no = int(input())

#player2 tries to guess the number in 10 attempts
tot_guesses = 10
current_guesses = 0

print(f"{player2} Guess the 4 digit number: ")
no_guessed = int(input())

while current_guesses<9:
    if no_guessed == no:
        current_guesses +=1
        print(f"Yay! {player2} you guessed the number in {current_guesses} guess. You are a MasterMind!!")
        break
    
    no = str(no)
    no_guessed = str(no_guessed)
    
    correct = ['x'] * 4
    count = 0

    # for loop runs 4 times since the number has 4 digits.
    for i in range(0,4):
        # checking for equality of digits
            if (no[i] == no_guessed[i]):
                # number of digits guessed correctly increments
                count += 1
                # hence, the digit is stored in correct[].
                correct[i] = no[i]
            else:
                continue

    # when none of the digits are guessed correctly.
    if no == no_guessed:
        # current gusses must be incremented when the n==num gets executed as we have the other incrmentation in the n!=num condition
        current_guesses += 1
        print("You've become a Mastermind!")
        print("It took you only", current_guesses, "tries.")
        break
    elif (count == 0):
        print("None of the numbers in your input match.")
        no_guessed = int(input("Enter your next choice of numbers: "))
        current_guesses +=1
        continue
    elif (count > 0):
        print("Not quite the number. But you did get ",count, " digit(s) correct!")
        print("Also these numbers in your input were correct.")
        for k in correct:
            print(k, end=' ')
        print()
        print()
        no_guessed = int(input("Enter your next choice of numbers: "))
        current_guesses +=1
        continue
