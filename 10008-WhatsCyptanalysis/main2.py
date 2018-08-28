import sys

def findMax(lst):
    maxIndex = 0
    for i in range(1,len(lst)):
        if lst[i] > lst[maxIndex]:
            maxIndex = i
    return maxIndex


n = sys.stdin.readline()
lst = [0] * 255
for i in sys.stdin.read():

    asciiVal = ord(i.upper())
    if lst[asciiVal] != 0:
        lst[asciiVal] += 1
    else :
        if asciiVal >= 65 and asciiVal <= 90:
            lst[asciiVal] = 1
    max = findMax(lst)
    print(lst[max])
    lst[max] = 0
# print(lst[64:89])

