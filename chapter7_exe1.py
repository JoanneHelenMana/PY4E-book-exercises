# Write a program to read through a file and print the contents of the file (line by line) all in upper case.

file = open('mbox-short.txt')
file_read = file.read()
file_read_upper = file_read.upper()
print(file_read_upper)
