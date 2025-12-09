# Number Guessing Game

from random import randint

def main():
    print(f"--- Welcome to Number Guessing Game ---")
    print("Guess numbers between 1 - 100")
    print()
    while True:
        play_game()
        print()
        if not get_choice("Do you want to replay? (y/n): "):
            print()
            print(f"--- Thank you for playing Number Guessing Game ---")
            print("Goodbye!")
            break


def generate_random_num():
    return randint(1, 100)


def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if 1 <= number <= 100:
                return number
            else:
                print("Number must be between 1-100")
        except ValueError:
            print("Invalid input type! Please input +ve integers")


def play_game():
    random_num = generate_random_num()

    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:

        guess = get_number(f"Attempt {attempts + 1}/{max_attempts} --> Guess: ")
        attempts += 1

        if guess == random_num:
            print()
            print("🎉 Congratulations! You've guessed the number")
            print(f"Attempts made = {attempts}")
            return

        elif guess < random_num:
            print("Too low!")
        else:
            print("Too large!")
    print()
    print("You've used your attempts limit!")
    print(f"The number was {random_num}")


def get_choice(prompt):
    while True:
        choice = input(prompt)
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print("Invalid Choice!")

main()
