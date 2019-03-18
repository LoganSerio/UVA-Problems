import sys
import re

line = sys.stdin.readline()
while line:
    sentence = re.split("( )", line.strip('\n'))
    buffer = ''
    for i in range(0,len(sentence)):
        sentence[i] = sentence[i][::-1]
        buffer = buffer + sentence[i]
        # if i == len(sentence)-1:
        #     buffer = buffer + sentence[i]
        # else:
        #     buffer = buffer + sentence[i] + ' '
    print(buffer)
    line = sys.stdin.readline()
