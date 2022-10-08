# Write another program that prompts for a list of numbers as above and at the end prints out
# both the maximum and minimum of the numbers instead of the average.


minimum = None
maximum = None

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        number = float(number)
    except:
        print('Invalid input. Enter a numeric value or "done".')
        continue

    if minimum is None:
        minimum = number
    if number < minimum:
        minimum = number
    if maximum is None:
        maximum = number
    if number > maximum:
        maximum = number

print(f'Maximum: {maximum}\nMinimum: {minimum}\n')
