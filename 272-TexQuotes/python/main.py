import sys

count = 1
for line in sys.stdin:
	for i in line:
		if i == "\"":
			if count%2 != 0:
				sys.stdout.write("``")
			else:
				sys.stdout.write("''")
			count += 1
		else:
			sys.stdout.write(i)
