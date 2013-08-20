#Project Euler 3
#20/08/13

from math import sqrt

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

#Method 1: start from that number, and work backwards?
#Nope: we need the list of primes to see if they are factors of that number

#Method 2: create list of primes up to half that number, then work backwards through that list checking if factor.

# plist=[2]
# pfactors=[]
# for i in range(2, int(13196/2)):
# 	for p in plist:
# 		if p>i/2 and p>3:
# 			break
# 		if i%p==0 and i!=p:
# 			if i in plist:
# 				plist.remove(i)
# 			break
# 		elif i%p!=0 and p!=1 and p!=i and i not in plist:
# 			plist.append(i)
# 			if 13195%i==0:
# 				pfactors.append(i)
# print(pfactors)
# print(pfactors[-1])

#Nope: this is slow, and gives us the largest factor that is prime of the given number, not the largest prime factor (??)


#Method 3: with an already populated list of primes, we shall use an algorithm which divides the number by a prime, then divides this number by other primes until it finds a prime.

#This sieve is not my code, 
def sieve(end):  
    if end < 2: return []  
    #The array doesn't need to include even numbers  
    lng = ((end//2)-1+end%2)  
    # Create array and assume all numbers in array are prime  
    sieve = [True]*(lng+1)  
    # In the following code, you're going to see some funky  
    # bit shifting and stuff, this is just transforming i and j  
    # so that they represent the proper elements in the array.  
    # The transforming is not optimal, and the number of  
    # operations involved can be reduced.  
    # Only go up to square root of the end  
    for i in range(int(sqrt(end)) >> 1):  
        # Skip numbers that aren’t marked as prime  
        if not sieve[i]: continue  
        # Unmark all multiples of i, starting at i**2  
        for j in range( (i*(i + 3) << 1) + 3, lng, (i << 1) + 3):  
            sieve[j] = False  
    # Don't forget 2!  
    primes = [2]  
    # Gather all the primes into a list, leaving out the composite numbers  
    primes.extend([(i << 1) + 3 for i in range(lng) if sieve[i]])  
    return primes

prime=n=600851475143
primeList=sieve(int(sqrt(prime)))
primeFactors=[]

i=0
while n>1:
	p=int(primeList[i])
	if n%p==0:
		n=int(n/p)
		primeFactors.append(p)
	else:
		i+=1
print(primeFactors[-1])