fhand = open('mbox-short.txt')

inp = fhand.read()
print(len(inp))
print(inp[:20])

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('Received:'):
        continue
    #if line.find('@uct.ac.za') == -1:
    #    continue
    print(line)
