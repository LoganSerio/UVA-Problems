import sys

def fn(n):
    if len(n) <= 1:
        return n
    else:
        lst = list(n)
        s = sum(int(x) for x in lst)
        return fn(str(s))

while True:
    line = sys.stdin.readline().replace('\n','')
    if line == '0':
        break
    print(fn(line))

