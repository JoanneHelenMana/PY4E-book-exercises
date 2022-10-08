"""
Add code to the above program to figure out who has the most messages in the file. After all the data
has been read and the dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many
messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
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

maximum_count = 0   # Sets counter at 0
maximum_email = ""  # Sets empty variable

for key in email_count:     # Searches through dictionary items
    if email_count[key] > maximum_count:    # Checks if new maximum
        maximum_count = email_count[key]    # Updates the maximum count
        maximum_email = key     # Updates the email address according to new maximum count

print(maximum_email, maximum_count)
