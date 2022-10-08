# Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg
# to their program. Modify the program that prompts the user for the file name so that it prints a
# funny message when the user types in the exact file name “na na boo boo”. The program should behave
# normally for all other files which exist and don’t exist. Here is a sample execution of the program:
#
# python egg.py
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt
# python egg.py
# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt
# python egg.py
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!
#
# We are not encouraging you to put Easter Eggs in your programs; this is just an exercise.
count = 0

file_name = input('Enter the file name:\n')
try:
    if file_name == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    file_handle = open(file_name)
except FileNotFoundError:
    print('File cannot be opened:', file_name)
    exit()

for line in file_handle:
    if line.startswith('Subject:'):
        count = count + 1

print(f'There were {count} subject lines in {file_name}.')
