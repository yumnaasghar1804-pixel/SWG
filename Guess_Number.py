import random

def number_guessing_game():
    print("🎯 Welcome to Number Guessing Game!")
    number = random.randint(1, 50)  # number between 1 and 50
    attempts = 0

    while True:
        guess = int(input("Enter your guess (1-50): "))
        attempts += 1

        if guess < number:
            print("⬆ Too low!")
        elif guess > number:
            print("⬇ Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

number_guessing_game()