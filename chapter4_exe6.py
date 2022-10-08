# Rewrite your pay computation with time-and-a-half for over-time
# and create a function called compute_pay which takes two parameters (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

rate = input('Enter rate:\n')
try:
    rate = float(rate)
except ValueError:
    print('Error, please enter a valid rate.')
    quit()

hours = input('Enter hours:\n')
try:
    hours = float(hours)
except ValueError:
    print('Error, please enter a valid number.')
    quit()


def computepay(hours, rate):
    if hours > 40:
        return (rate * 40) + ((hours - 40) * (rate * 1.5))
    else:
        return hours * rate


print(f'Your gross pay is ${computepay(hours, rate)}.')
