# Write a while loop that starts at the last character in the string and works its way backwards
# to the first character in the string, printing each letter on a separate line, except backwards.

fruit = 'apple'
index = len(fruit) - 1

# WHILE LOOP
while index >= 0:
    letter = fruit[index]
    print(letter)
    index = index - 1

# FOR LOOP
for char in fruit:
    print(fruit[index])
    index = index - 1
