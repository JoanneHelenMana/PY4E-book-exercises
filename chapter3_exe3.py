# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range,
# print an error message.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score	Grade
# >= 0.9 	A
# >= 0.8 	B
# >= 0.7 	C
# >= 0.6 	D
# < 0.6     F

# Enter score: 0.95
# A
#
# Enter score: perfect
# Bad score
#
# Enter score: 10.0
# Bad score
#
# Enter score: 0.75
# C
#
# Enter score: 0.5
# F
#
# Run the program repeatedly as shown above to test the various values for input.

score = input('Enter score:\n')
try:
    score = float(score)
    if score > 1.0 or score < 0.0:
        print('Error. Score out of range.')
    elif 1.0 >= score >= 0.9:
        print('A')
    elif 0.9 > score >= 0.8:
        print('B')
    elif 0.8 > score >= 0.7:
        print('C')
    elif 0.7 > score >= 0.6:
        print('D')
    elif 0.6 > score >= 0.0:
        print('F')
except ValueError:
    print('Error. Please enter a valid numeric score.')
