import sys

testcases = int(sys.stdin.readline())

for i in range(0,testcases):
	n = int(sys.stdin.readline())
	n = int((((((n*567)/9)+7492)*235)/47)-498)
	n = str(n)
	print(n[-2:-1])
