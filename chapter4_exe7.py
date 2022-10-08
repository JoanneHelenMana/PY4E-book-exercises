# Rewrite the grade program from the previous chapter using a function called computegrade
# that takes a score as its parameter and returns a grade as a string.
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
#
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
#
# Run the program repeatedly to test the various different values for input.

def compute_grade(score):
    if score > 1.0 or score < 0.0:
        return 'Error. Score out of range.'
    elif 1.0 >= score >= 0.9:
        return 'A'
    elif 0.9 > score >= 0.8:
        return 'B'
    elif 0.8 > score >= 0.7:
        return 'C'
    elif 0.7 > score >= 0.6:
        return 'D'
    elif 0.6 > score >= 0.0:
        return 'F'


score = input('Enter score:\n')
try:
    score = float(score)
    print(compute_grade(score))
except ValueError:
    print('Error. Please enter a valid numeric score.')
