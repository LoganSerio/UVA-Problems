import sys

def f91(n):
	if n >= 101:
		return n - 10;
	else:
		return 91;

for line in sys.stdin.readline():
	line = int(line)
	print(line)
	if str(line) == 0:
		break
	else:
		print "f91(%s)" %line
