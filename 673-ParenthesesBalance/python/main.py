import sys

left = ['[','(']
right = [']',')']
cases = int(sys.stdin.readline())
for i in range(cases):
    bal = True
    stack = []
    str = sys.stdin.readline().strip('\n')
    for letter in str:
        if letter in left:
            stack.append(letter)
        else:
            if len(stack) == 0:
                bal = False
            else:
                popVal = stack.pop()
                if letter == ')' and popVal != '(':
                    bal = False
                elif letter == ']' and popVal != '[':
                    bal = False
    if len(stack) > 0 or not bal:
        print('No')
    else:
        print('Yes')
        