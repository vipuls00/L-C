import random

def is_valid_guess(user_input):
    if user_input.isdigit() and 1 <= int(user_input) <= 100:
        return True
    else:
        print("Invalid input. Please enter a number between 1 and 100.")
        return False

def get_user_guess():
    while True:
        user_input = input("Guess a number between 1 and 100: ")
        if is_valid_guess(user_input):
            return int(user_input)

def provide_feedback(guess, target):
    if guess < target:
        print("Too low. Guess again.")
        return False
    elif guess > target:
        print("Too high. Guess again.")
        return False
    else:
        print("Congratulations! You guessed it!")
        return True

def main():
    target_number = random.randint(1, 100)
    guess_count = 0
    guessed_correctly = False

    while not guessed_correctly:
        user_guess = get_user_guess()
        guess_count += 1
        guessed_correctly = provide_feedback(user_guess, target_number)

    print(f"You guessed the number in {guess_count} attempts.")

if __name__ == "__main__":
    main()
