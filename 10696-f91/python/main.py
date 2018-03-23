import sys
def f91(n):
	#if len(cache)-1 < n:
		#if cache[n] is not 0:
		#	return cache[n];
	if n >= 101:
		#res = f91(f91(n+11));
		#cache.insert(n,res)
		return n - 10;
	
	else:
		#res = n - 10;
		#cache.insert(n,res)
		return 91;

for line in sys.stdin.readlines():
	line = int(line)
	if line == 0:
		break
	else:
		print("f91("+str(line)+") = "+str(f91(line)))
