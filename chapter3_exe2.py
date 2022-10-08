# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully
# by printing a message and exiting the program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

payRate = input('Enter rate:\n')
try:
    payRate = float(payRate)
except ValueError:
    print('Error, please enter numeric input.')
    quit()

hours = input('Enter hours:\n')
try:
    hours = float(hours)
except ValueError:
    print('Error, please enter numeric input.')
    quit()

pay = payRate * hours
if hours > 40:
    pay = payRate * 40 + ((hours - 40) * (payRate * 1.5))
    print('Pay:', pay)
