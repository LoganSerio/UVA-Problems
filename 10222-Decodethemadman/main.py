import sys
import re
firstRow = ['q','w','e','r','t','y','u','i','o','p','[',']','\\']
secondRow = ['a','s','d','f','g','h','j','k','l',';','\'']
thirdRow = ['z','x','c','v','b','n','m',',','.','/']

line = sys.stdin.readline().lower()
while line:
    words = re.split('( )',line.strip('\n'))
    for i in range(0,len(words)):
        letterlist = list(words[i])
        for j in range(0,len(letterlist)):
            if letterlist[j] in firstRow:
                letterlist[j] = firstRow[firstRow.index(letterlist[j])-2]

            elif letterlist[j] in secondRow:
                letterlist[j] = secondRow[secondRow.index(letterlist[j])-2]

            elif letterlist[j] in thirdRow:
                letterlist[j] = thirdRow[thirdRow.index(letterlist[j])-2]

        words[i] = ''.join(letterlist)
    print(''.join(words))
    line = sys.stdin.readline().lower()
