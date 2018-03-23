import sys

testcases = int(sys.stdin.readline())
for x in range(0,testcases):
	count = int(sys.stdin.readline())
	perm = [int(x) for x in sys.stdin.readline().split()]
	done = False
	swaps = 0
	while not done:
		done = True
		for i in range(1,count):
			if perm[i-1] > perm[i]:
				done = False
				swaps += 1
				tmp = perm[i-1]
				perm[i-1] = perm[i]
				perm[i] = tmp
			#else:
			#	print(perm)
	print("Optimal train swapping takes " + str(swaps) + " swaps.")
				
