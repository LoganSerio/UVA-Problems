import sys

cases = int(sys.stdin.readline())

for i in range(0,cases):
    sys.stdin.readline()
    amp = int(sys.stdin.readline())
    freq = int(sys.stdin.readline())
    for x in range(freq):
        buffer = ''
        for curAmp in range(1,2*amp):
            if curAmp > amp:
                buffer += str(2*amp-curAmp)*(2*amp-curAmp) + '\n'
            else:
                buffer += (str(curAmp)*curAmp) +'\n'
        if i == cases-1 and x == freq-1:
            sys.stdout.write(buffer)
        else:
            print(buffer)