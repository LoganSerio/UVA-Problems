import sys

for line in sys.stdin:
	a = int(line)
	if a == 2:
		print("00\n01\n81")
	elif a == 4:
		print("0000\n0001\n2025\n3025\n9801")
	elif a ==  6:
		print("000000\n000001\n088209\n494209\n998001")
	else:
		print("00000000\n00000001\n04941729\n07441984\n24502500\n25502500\n52881984\n60481729\n99980001")

