import pandas

# Load the NATO phonetic alphabet data from CSV file
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary mapping letters to phonetic codes
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# Print the phonetic dictionary (for reference)
print(phonetic_dict)

# Prompt user input for a word to convert to NATO phonetic code
word = input("Enter a word: ").upper()

# Convert each letter in the input word to its NATO phonetic code
output_list = [phonetic_dict[letter] for letter in word]

# Print the list of NATO phonetic codes for the input word
print(output_list)
