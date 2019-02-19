import sys
import math

def main():
    inpt = get_input()
    print('PERFECTION OUTPUT')
    for case in inpt:
        sum = 0
        sum = sumDivisors(case)
        print(output(case,sum))
    print('END OF OUTPUT')

def get_input():
    inpt = sys.stdin.readline().split(' ')
    inpt = inpt[:len(inpt)-1]
    return list(map(int,inpt))

def sumDivisors(num):
    divs = set()
    i = 1
    while i <= math.sqrt(num):
        if num%i == 0:
            divs.add(i)
            divs.add(num//i)
        i += 1
    divs.remove(num)
    return sum(x for x in divs)

def output(num,sum):
    word = 'PERFECT'
    if num > sum:
        word = 'DEFICIENT'
    elif num < sum:
        word = 'ABUNDANT'
    return '{:>5}'.format(str(num)) + '  ' + word
    
main()

#if __name__ == "__main__": main()
