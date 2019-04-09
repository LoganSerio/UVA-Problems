import sys
import re

buff = []
sent = []
max = 0
for line in sys.stdin.readlines():
    if len(line) > max:
        max = len(line)
    sent.append(line.strip('\n'))
sent = sent[::-1]

for i in range(0,max):
    tmp = ''
    for j in range(0,len(sent)):
        if len(sent[j])-1 >= i:
            tmp += sent[j][i]
        else: 
            tmp += ' '
    if tmp:
    # if not tmp.isspace():
        buff.append(tmp)
        # print(tmp)
for l in buff:
    print(l)