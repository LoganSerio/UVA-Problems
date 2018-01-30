import sys

n = sys.stdin.readline()
for i in range(0,int(n)):
	f = sys.stdin.readline()
	sum = 0
	for j in range(0, int(f)):
		line = sys.stdin.readline()
		land, animals, enviro = line.split()
		totprem = int(enviro) * int(land)
		if int(animals) == 0:
			totprem = 0
		sum += totprem
	print(sum)
