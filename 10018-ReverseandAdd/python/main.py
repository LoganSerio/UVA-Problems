import sys

n = int(sys.stdin.readline())
for i in range(0,n):
	sum = 0
	init = sys.stdin.readline()
	sum += int(init)
	iterations = 0
	isFirst = True
	while str(sum) != str(sum)[::-1] or isFirst:
		if isFirst:
			isFirst = False
		reverse = int(str(sum)[::-1])
		sum += reverse
		iterations += 1
	print(str(iterations) + " " + str(sum)) 
	
	
