"""
Morse Code Translator — converts text to Morse code and back.
"""

MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
    "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.",
    "$": "...-..-", "@": ".--.-.",
}

REVERSE_MORSE = {code: letter for letter, code in MORSE_CODE.items()}


def text_to_morse(text):
    words = text.upper().split(" ")
    morse_words = []
    for word in words:
        letters = [MORSE_CODE.get(ch, "") for ch in word]
        morse_words.append(" ".join(filter(None, letters)))
    return " / ".join(morse_words)


def morse_to_text(morse):
    morse_words = morse.strip().split(" / ")
    text_words = []
    for word in morse_words:
        letters = [REVERSE_MORSE.get(code, "") for code in word.split(" ") if code]
        text_words.append("".join(letters))
    return " ".join(text_words)


def main():
    menu = """
1. Text to Morse code
2. Morse code to Text
3. Exit
"""
    print("=== Morse Code Translator ===")
    print("(Separate words with ' / ' when entering Morse code)")

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            text = input("Enter text: ")
            print(f"\nMorse code: {text_to_morse(text)}")

        elif choice == "2":
            morse = input("Enter Morse code: ")
            print(f"\nText: {morse_to_text(morse)}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
