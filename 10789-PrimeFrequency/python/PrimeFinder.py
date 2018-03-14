import sys,math

#primes = []

#n = 10
#for i in range(2,n+1):
#	count = 1
#	if i not in primes:	
#		for j in range(i*i,n+1,i):
#			primes.append(j)
#			
#print(primes)
n = 2000	
not_prime = []
prime = []
for i in xrange(2, n+1):
    if i not in not_prime:
        prime.append(i)
        for j in xrange(i*i, n+1, i):
            not_prime.append(j)
print(prime)			
