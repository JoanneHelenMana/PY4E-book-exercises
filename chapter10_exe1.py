"""
Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from
the line. Count the number of messages from each person using a dictionary. After all the data has been
read, print the person with the most commits by creating a list of (count, email) tuples from the
dictionary. Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
"""
email_count = dict()

file = open('mbox.txt', 'r')

for line in file:
    if line.startswith('From '):
        words = line.split()  # Splits string line into string words
        email = words[1]  # Retrieves second word in line (the email address)
        email_count[email] = email_count.get(email, 0) + 1  # Adds new key into dictionary with count.
        # If key already exists, it modifies value by increasing the count.

lst = list()    # Initialises an empty list

for key, val in list(email_count.items()):  # Displays items in dictionary as list, and iterates through keys and values
    lst.append((val, key))  # Adds values and keys -in that order- to the list

lst.sort(reverse=True)  # Sorts list by highest value

for key, val in lst[:1]:    # Iterates through items before [1]
    print(key, val)     # Displays the highest value
