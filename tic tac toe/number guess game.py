import random

target = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < target:
        print("Too low! Try again.")
    elif guess > target:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
