import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
all_words = {row.letter: row.code for (index, row) in data.iterrows()}
print(all_words)


def nato_phonetic():
    user_input = input("Enter a word").upper()
    try:
        output = [all_words[letter] for letter in user_input]
    except KeyError:
        print("Enter all alphabets")
        nato_phonetic()
    else:
        print(output)


nato_phonetic()
