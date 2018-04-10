import sys

inpt = sys.stdin.readlines()
for line in inpt:
	buff = ""
	for char in line:
		if char == '\n':
			buff = buff + '\n'
		else:
			buff = buff + chr(ord(char)-7)
	print(buff)
