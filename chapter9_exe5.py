"""
This program records the domain name (instead of the address) where the message was sent from instead
of who the mail came from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""
domain_count = dict()  # Creates empty dictionary

file = open('mbox.txt', 'r')
for line in file:
    if line.startswith('From '):  # Identifies lines that begin with 'From ' only
        words = line.split()  # Splits string line into string words
        email = words[1]  # Retrieves second word in line (the email address)
        at = email.find('@')    # Finds the character where to stop
        domain = email[at+1:]   # Slices the email to obtain the domain only

        domain_count[domain] = domain_count.get(domain, 0) + 1  # Adds new key into dictionary. If key already exists,
        # it modifies value by increasing the count

print(domain_count)
