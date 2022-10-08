"""
Write a program to read through a mail log, build a histogram using a dictionary to count
how many messages have come from each email address, and print the dictionary.
Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
"""
email_count = dict()  # Creates empty dictionary

file = open('mbox.txt', 'r')
for line in file:
    if line.startswith('From '):  # Identifies lines that begin with 'From ' only
        words = line.split()  # Splits string line into string words
        email = words[1]  # Retrieves second word in line (the email address)
        email_count[email] = email_count.get(email, 0) + 1  # Adds new key into dictionary. If key already exists,
        # it modifies value by increasing the count

print(email_count)
