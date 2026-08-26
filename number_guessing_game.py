import random


def number_guessing_game():
    print("===== Number Guessing Game =====")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempt(s).")
                break

        except ValueError:
            print("Please enter a valid number.")


number_guessing_game()
