"""
Figure out which line of the program below is still not properly guarded. See if you can construct a
text file which causes the program to fail and then modify the program so that the line is properly
guarded and test it to make sure it handles your new text file:

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])
"""

fhand = open('mbox.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From': continue
    print(words[2])
