"""
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
    count = count + 1
print(count)

Encapsulate this code in a function named count, and generalize it
so that it accepts the string and the letter as arguments.
"""
def count(word, letter):
    counter = 0
    for char in word:
        if char == letter:
            counter = counter + 1
    return counter


word = input('Enter a word:\n')
letter = input('Enter a letter in that word to be counted:\n')
print(f'The word "{word}" has {count(word, letter)} "{letter}".')
