import sys

def main():
    inpt = get_input()
    i = 1
    for case in inpt:
        leader = findLeader(case)
        output(i,leader)
        i += 1


def get_input():
    testcases = int(sys.stdin.readline())
    lines = []
    while testcases > 0:
        inpt = sys.stdin.readline().strip('\n').split(" ")
        lines.append(list(map(int,inpt)))
        testcases -= 1
    return lines
        
def findLeader(case):
    case.sort
    return case[len(case)//2]

def output(num, leader):
    print('Case ' + str(num) +": "+str(leader))

main()