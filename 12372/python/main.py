import sys

tc = int(sys.stdin.readline())

for i in range(tc):
    l,w,h = sys.stdin.readline().split()
    if int(l) > 20 or int(w) > 20 or int(h) > 20:
        print('Case ' + str(i+1) + ': bad' )
    else:
        print('Case ' + str(i+1) + ': good')
