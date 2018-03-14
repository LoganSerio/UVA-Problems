import sys

ugly = [1,2,3,4,5,6,8,9,10,12,15]

count = 16
uglyCount = 11
while len(ugly) <= 1500:
	if count % 2 == 0 or count % 3 == 0 or count % 5 == 0:
		ugly.append(count)
		count += 1
print("The 1500'th ugly number is "+ str(ugly[len(ugly)-1]) +".") 
