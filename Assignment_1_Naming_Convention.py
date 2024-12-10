# Assignment 1: Dice Roller Program
import random

def roll_dice(sides_of_dice):
    rolled_value = random.randint(1, sides_of_dice)
    return rolled_value

def roll_dice_game():
    sides_of_dice = 6
    continue_rolling = True
    while continue_rolling:
        user_input = input("Ready to roll? Enter Q to Quit: ")
        if user_input.lower() != "Q":
            rolled_number = roll_dice(sides_of_dice)
            print("You have rolled a", rolled_number)
        else:
            continue_rolling = False

#Assignment 2: Number Guessing Game

def is_valid_input(user_input):
    if user_input.isdigit() and 1 <= int(user_input) <= 100:
        return True
    else:
        return False

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guessed_correctly = False
    user_guess = input("Guess a number between 1 and 100: ")
    guess_count = 0

    while not guessed_correctly:
        if not is_valid_input(user_guess):
            user_guess = input("I won't count this one. Please enter a number between 1 and 100: ")
            continue
        else:
            guess_count += 1
            user_guess = int(user_guess)

        if user_guess < number_to_guess:
            user_guess = input("Too low. Guess again: ")
        elif user_guess > number_to_guess:
            user_guess = input("Too high. Guess again: ")
        else:
            print(f"You guessed it in {guess_count} guesses!")
            guessed_correctly = True

guess_the_number()

# Assignment 3: Armstrong Number Check

def check_armstrong_num(input_number):
    armstrong_sum = 0
    digit_count = 0

    current_number = input_number
    while current_number > 0:
        digit_count += 1
        current_number = current_number // 10

    current_number = input_number
    for _ in range(digit_count):
        remainder = current_number % 10
        armstrong_sum += remainder ** digit_count
        current_number //= 10

    return armstrong_sum

# End of Function

# User input
number_to_check = int(input("\nPlease Enter the Number to Check for Armstrong: "))

if number_to_check == check_armstrong_num(number_to_check):
    print(f"\n{number_to_check} is an Armstrong Number.\n")
else:
    print(f"\n{number_to_check} is Not an Armstrong Number.\n")
