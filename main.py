import pandas

# TODO 1. Create a dictionary in this format:

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

data = {row.letter: row.code for (index, row) in alphabet.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word you want to generate nato phonetic for: ").upper()

output = [data[char] for char in user_input]

print(output)
