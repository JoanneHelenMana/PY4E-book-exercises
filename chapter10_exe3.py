"""
Write a program that reads a file and prints the letters in decreasing order of frequency.
Your program should convert all the input to lower case and only count the letters a-z.
Your program should not count spaces, digits, punctuation, or anything other than the
letters a-z. Find text samples from several different languages and see how letter
frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.
"""
import string

letter_count = dict()   # Initialises variables
lst = list()

text = input('Enter file name:\n')  # Prompts file and language
language = input('Enter language:\n')

file = open(text, 'r')

for line in file:   # Removes number and punctuation, and sets to lowercase
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.lower()

    words = line.split()    # Splits strings of lines into strings of words
    for word in words:
        for letter in word:     # Iterates through each character
            letter_count[letter] = letter_count.get(letter, 0) + 1  # If letter is not
            # in the dictionary, it adds it, and computes frequency

for key, val in list(letter_count.items()):     # Iterates through items in the list
    lst.append((val, key))  # Adds frequency, letter of dictionary to the list

lst.sort(reverse=True)  # Sorts list in decreasing order

for key, val in lst:
    print(key, val)     # Prints frequency, letter

for key, val in lst[:1]:
    most_frequent_letter = val  # Retrieves the most frequent letter

print(f"The most frequent letter in {language} is '{most_frequent_letter}'.")
