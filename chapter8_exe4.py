"""
Create a list of unique words, which will contain the final result.
Write a program to open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split function. For each word, check to see
if the word is already in the list of unique words. If the word is not in the list of unique words,
add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.
"""
unique_words = []
text = open('romeo.txt', 'r')
for line in text:
    words = line.split()    # Splits line into array of words
    for word in words:
        if word in unique_words: continue   # Discards duplicates
        unique_words.append(word)   # Adds word to list

unique_words.sort() # Sorts list
print(unique_words.sort())
