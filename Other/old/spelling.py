from spellchecker import SpellChecker

spell = SpellChecker()

# Example sentence with typos
text = "I liek to lern machien lerning"

# Split sentence into words
words = text.split()

# Correct words
corrected_words = [spell.correction(word) for word in words]

# Join back into sentence
corrected_text = " ".join(corrected_words)

print("Before:", text)
print("After:", corrected_text)
