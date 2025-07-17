# Random Number Guessing Game (0 to 10)

import random

SECRET = random.randint(0, 10)
MAX_ATTEMPTS = 5
attempts = 0

print("🎲 Welcome to the Number Guessing Game!")
print("Guess a number between 0 and 10. You have 5 tries.")

while attempts < MAX_ATTEMPTS:
    try:
        guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess → "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    if guess == SECRET:
        print("🎉 Correct! You guessed the number.")
        break
    elif guess > SECRET:
        print("📈 Too high!")
    else:
        print("📉 Too low!")

    attempts += 1

    if attempts == MAX_ATTEMPTS:
        print(f"\n😢 You're out of attempts. The correct number was {SECRET}.")
    elif attempts == 3:
        print("⚠️ You have 2 attempts left.")

print("✅ Game Over. Thanks for playing!")