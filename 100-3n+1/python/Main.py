import sys

cache = {}
def num_cycles(num):
	if num in cache:
		return cache[num]
	if num <= 1:
		return 1
	orig = num
	if num%2 != 0:
		 num = 3*num+1
	else:
		num = num/2
	count = 1 + num_cycles(num)
	cache[orig] = count
	return count
	
	
for line in sys.stdin:
	i,j = line.split()
	maxOf= 0
	if int(i) < int(j):
		i1 = i
		j1 = j
	else:
		i1 = j
		j1 = i
	for x in range(int(i1),int(j1)+1):
		maxOf = max(num_cycles(x),maxOf)
	print(i + " " + j + " " + str(maxOf)) 
	
