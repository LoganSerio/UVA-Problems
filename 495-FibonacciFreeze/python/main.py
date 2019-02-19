import sys

cache = [-1]*5001
cache[0] = 0
cache[1] = 1
cache[2] = 1

def getInput():
    inpt = []
    lines = sys.stdin.readlines()
    for line in lines:
        if line!="":
            inpt.append(int(line))
    return inpt

def fib(n):
    if cache[n] != -1:
        return cache[n]
    else:
        res = fib(n-1) + fib(n-2)
        cache[n] = res

def output(inpt):
    for num in inpt:
        print("The Fibonacci number for " +str(num) +" is "+ str(cache[num]))

def fillCache():
    for i in range(0,5001):
        fib(i)

def main():
    fillCache()
    output(getInput())


if __name__ == "__main__": main()