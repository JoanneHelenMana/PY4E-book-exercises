"""
Write a program that categorizes each mail message by which day of the week the commit was done.
To do this look for lines that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print out the contents of your
dictionary (order does not matter).

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""
day_count = dict()  # Creates empty dictionary
file = open('mbox.txt', 'r')
for line in file:
    if line.startswith('From '):
        words = line.split()
        day = words[2]  # Retrieves third word in line (the day)
        if day not in day_count:
            day_count[day] = 1  # Enters key(day) into dictionary and adds value(count)
        else:
            day_count[day] += 1  # Finds if key in already in the dictionary and increments count(value)

print(day_count)
