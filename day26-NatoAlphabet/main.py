# With open file
name = input("Enter your name: ").upper()

with open("nato_phonetic_alphabet.csv") as file:
    data = file.readlines()
    nato_dict = {row.split(",")[0]: row.split(",")[1].strip() for row in data}

    translate = [nato_dict[letter] for letter in name if letter in nato_dict]

print(translate)

# With pandas
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (_, row) in data.iterrows()}

name = input("Enter your name: ").upper()
result = [nato_dict[letter] for letter in name if letter in nato_dict]

print(result)
