import sys

two = ['A','B','C']
three = ['D','E','F']
four = ['G','H','I']
five = ['J','K','L']
six = ['M','N','O']
seven = ['P','Q','R','S']
eight = ['T','U','V']
nine = ['W','X','Y','Z']

line = sys.stdin.readline()
while line:
    line = list(line.strip('\n'))
    for i in range(len(line)):
        if line[i] in two:
            line[i] = '2'
        elif line[i] in three:
            line[i] = '3'
        elif line[i] in four:
            line[i] = '4'
        elif line[i] in five:
            line[i] = '5'
        elif line[i] in six:
            line[i] = '6'
        elif line[i] in seven:
            line[i] = '7'
        elif line[i] in eight:
            line[i] = '8'
        elif line[i] in nine:
            line[i] = '9'
    print(''.join(line))
    line = sys.stdin.readline()