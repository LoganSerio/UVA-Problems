import sys, re

for line in sys.stdin:
	line2 = re.split("[^a-zA-Z]*",line)
	line2 = list(filter(None,line2))
	print(len(line2))
	
