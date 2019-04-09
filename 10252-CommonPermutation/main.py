import sys

lines = sys.stdin.readlines()
inpt = []
# for l in range(0,len(lines)):
#     if lines[l].strip():
#         inpt.append(lines[l].strip())
inpt = list(filter(None,lines))
for i in range(1,len(inpt),2):
    a = inpt[i-1].strip()
    b = inpt[i].strip()
    commonPerm = ''
    for letter in a:
        if letter in b:
            commonPerm += letter
    print(''.join(sorted(commonPerm)))
    