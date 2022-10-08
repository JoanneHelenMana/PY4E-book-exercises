"""
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.
"""
count = 0
words_dict = dict()     # Creates an empty dictionary
file = open('words.txt', 'r')
for line in file:   # Reads file line by line
    words = line.split()    # Splits text into words
    for word in words:
        count += 1  # Indicates order of appearance of every new word
        if word in words_dict:  # Ignores repeated words
            continue
        words_dict[word] = count    # Adds every new word to the dictionary

while True:
    word_enter = input('Enter word:\n')
    if word_enter == 'done':
        break
    elif word_enter in words_dict:
       print(f'"{word_enter}" appears in the text.')
    elif word_enter not in words_dict:
      print(f'"{word_enter}" does not appear in the text.')
