import sys

for line in sys.stdin:
	v,t = line.split()
	v = int (v)
	t = int (t)
	print(v*(2*t))
