# #100days of code - day 26 - NATO Alphabet

import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}  # list comprehension
print(alphabet_dict)


def user_input():
    word = input("Enter a word: ").upper()

    # without loop - dictionary comprehension
    try:
        phonetic_word2 = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Only letters in the alphabet please.")
        user_input()
    else:
        print(phonetic_word2)


user_input()

# with loop
# phonetic_word = []
# for letter in word:
#     ph_letter = alphabet_dict[letter]
#     phonetic_word.append(ph_letter)

# print(phonetic_word)


# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#


# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
