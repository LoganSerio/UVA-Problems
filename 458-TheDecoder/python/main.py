import sys

for line in sys.stdin:
	buff = ""
	for char in line:
		buff = buff + chr(ord(char)-7)
	print(buff)
