"""
Hangman Game — classic word-guessing game with ASCII art and limited guesses.
"""
import random

WORDS = [
    "python", "developer", "keyboard", "function", "variable",
    "algorithm", "computer", "internet", "software", "hangman",
]

STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """,
]

MAX_WRONG = len(STAGES) - 1


def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong_guesses = 0

    print("=== Hangman ===")

    while wrong_guesses < MAX_WRONG:
        display = " ".join(letter if letter in guessed else "_" for letter in word)
        print(STAGES[wrong_guesses])
        print(f"Word: {display}")
        print(f"Wrong guesses left: {MAX_WRONG - wrong_guesses}")

        if all(letter in guessed for letter in word):
            print("\nYou won! The word was:", word)
            return

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.add(guess)

        if guess not in word:
            wrong_guesses += 1
            print(f"'{guess}' is not in the word.\n")
        else:
            print(f"Good guess! '{guess}' is in the word.\n")

    print(STAGES[wrong_guesses])
    print(f"You lost! The word was: {word}")


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
