# Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered,
# print out the total, count, and average of the numbers. If the user enters anything other than a number,
# detect their mistake using try and except and print an error message and skip to the next number.
#
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

total = 0
count = 0
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        number = float(number)
    except:
        print('Invalid input. Enter a numeric value or "done".')
        continue
    count += 1
    total += number

average = total / count
print(f'Total: {total}\nCount: {count}\nAverage: {average}')
