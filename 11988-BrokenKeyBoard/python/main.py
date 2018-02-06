import sys

for line in sys.stdin:
	n = len(line)
	for i in range(0,n-1):
		print(line[i])
