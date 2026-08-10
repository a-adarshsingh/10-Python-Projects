!pip install pyspellchecker
from spellchecker import SpellChecker

spell = SpellChecker()

def spell_checker(text):
    words = text.split()
    corrected_words = []

    for word in words:
        correction = spell.correction(word)

        if correction != word.lower():
            print(f"{word} → {correction}")

        corrected_words.append(correction)

    return " ".join(corrected_words)


text = input("Enter a sentence: ")

result = spell_checker(text)

print("\nCorrected Sentence:")
print(result)
