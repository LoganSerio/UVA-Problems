import sys

left = ['(','[','{','<',';']
right = [')',']','}','>',':']
for line in sys.stdin.readlines():
    line = line.replace('(*',';')
    line = line.replace('*)',':')
    stack = []
    breakVal = -1
    bal = True
    for i in range(0,len(line)):
        char = line[i]
        if char in left:
            stack.append(char)
        elif char in right:
            if stack:
                p = stack.pop()
                indx = left.index(p)
                if right[indx] != char:
                    if breakVal == -1:
                        breakVal = i
                    bal = False
                    
            else:
                if breakVal == -1:
                    breakVal = i
                bal = False
    if len(stack) > 0:
        print('NO ' + str(len(line)))
    elif not bal: 
        print('NO ' + str(breakVal+1))
    else:
        print('YES')         