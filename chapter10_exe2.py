"""
This program counts the distribution of the hour of the day for each of the messages.
You can pull the hour from the “From” line by finding the time string and then splitting that string
into parts using the colon character. Once you have accumulated the counts for each hour,
print out the counts, one per line, sorted by hour as shown below.
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""
hour_count = dict()     # Initiates empty dictionary

file = open('mbox.txt', 'r')

for line in file:
    if line.startswith('From '):
        words = line.split()
        time = words[5]  # Retrieves the sixth word in line (the time)
        colon = time.find(':')
        hour = time[:colon]     # Slices the string to get the hour
        hour_count[hour] = hour_count.get(hour, 0) + 1  # Adds new key into dictionary with count.
        # If key already exists, it modifies value by increasing the count.

lst = list()    # Initialises an empty list

for key, val in list(hour_count.items()):  # Displays items in dictionary as list, and iterates through keys and values
    lst.append((key, val))  # Adds hour, count of dictionary to the list

lst.sort()

for key, val in lst:    # Iterates through items in the list
    print(key, val)
