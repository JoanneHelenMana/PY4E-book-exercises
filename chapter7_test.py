test = open('test.txt', 'w')
print(test)
line1 = 'is this for real?\n'
test.write(line1)
line2 = 'yes, it is'
test.write(line2)
test.close()
