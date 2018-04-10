import sys

testcases = int(sys.stdin.readline())

for line in range(0,testcases):
	line = list(sys.stdin.readline().split())
	n = int(line[0])
	l = len(line)
	line = line[1:l]
	sum = 0
	for i in line:
		sum = sum + int(i)
	avg = sum/n
	abvAvg = 0
	for j in line:
		if int(j) > avg:
			abvAvg += 1
	percent = 100*(abvAvg/n)
	print("%.3f%%" %percent) 	
