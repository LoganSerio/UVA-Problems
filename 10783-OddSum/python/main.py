import sys

n = int(sys.stdin.readline())
for i in range(0, n):
	a = int(sys.stdin.readline())
	b = int(sys.stdin.readline())
	if a > b:
		tmp = a
		a = b
		b = tmp
	sum = 0
	for x in range(a,b+1):
		if x % 2 != 0:
			sum += x
	print("Case " + str(i+1) + ": " +str(sum))	
