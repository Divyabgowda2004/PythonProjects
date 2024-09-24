import random

print("Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the game")

number_to_guess = random.randrange(100)
chances = 7
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    guess = int(input("Please enter your guess within 0-100: "))

    if guess == number_to_guess:
        print(f'The number is {guess} and you found it right! in the {guess_counter} attempt')
        break
    elif guess_counter >= chances and guess != number_to_guess:
        print(f'Oops sorry, The number is {number_to_guess} better luck next time')
    elif guess > number_to_guess:
        print("Your guess is higher")
    elif guess < number_to_guess:
        print('Your guess is lesser')
    
