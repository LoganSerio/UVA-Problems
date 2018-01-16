import sys

def num_cycles(num):
	if num == 1:
		return 1
	elif num%2 != 0:
		return (1+num_cycles(3*num+1))
	else:
		return (1+num_cycles(num/2))
	
for line in sys.stdin:
	i,j = line.split()
	max = 0
	for x in range(int(i),int(j)):
		n = num_cycles(x)
		if n > max:
			max = n
	print(i + " " + j + " " + str(max)) 
	
