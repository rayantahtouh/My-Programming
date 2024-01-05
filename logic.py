print("Welcome to the Number Guessing Game!")
print("I have selected a secret number between 1 and 10.")

# User input for the guess
user_guess = int(input("Guess the number: "))

# Secret number (but with a logical error)
secret_number = 7  # The secret number is always 7, but the user doesn't know that

# Check if the user's guess is correct
if user_guess == secret_number:
    Print("Congratulations! You guessed the correct number!")
else:
    Print(f"Oops! You guessed {user_guess}, but the secret number is {secret_number}. Better luck next time!")