import sys
n = sys.stdin.readline().strip('\n')
lst = []
while n: 
    cnt = 0
    lst = sys.stdin.readline().strip('\n').split(' ')
    for i in range(int(n)):
        for j in range(i+1,int(n)):
            if int(lst[i]) > int(lst[j]):
                cnt += 1
    print('Minimum exchange operations : ' + str(cnt))
    n = sys.stdin.readline().strip('\n')