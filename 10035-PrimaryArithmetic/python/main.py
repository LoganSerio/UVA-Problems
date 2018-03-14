import sys

for line in sys.stdin.readlines():
	top,bottom = line.split()
	carryCount = 0
	topArr = list(top)
	bottomArr = list(bottom)
	#Loop through the arrays from back to front and 
	#add the elements together. if the sum is greator than 9 then we
	#want to  carry
	#if len(topArr) > len(bottomArr):
	#	for i in range(
	top = int(top)
	bottom = int(bottom)	
	if carryCount < 2:
		print(str(carryCount) + " carry operation.")
	else:
		print(str(carryCount) + " carry operation.")
		
