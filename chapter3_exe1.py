# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate
# for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

payRate = float(input('Enter rate:\n'))
hours = int(input('Enter hours:\n'))

pay = payRate * hours
if hours > 40:
    pay = payRate * 40 + ((hours - 40) * (payRate * 1.5))
    print(pay)

