import sys, re

for line in sys.stdin:
	line2 = re.split("[^a-zA-Z]*",line)
	line2 = filter(None,line2)
	print(len(line2))
