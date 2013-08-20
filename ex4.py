#Project Euler 4
#20/08/13

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

palindrome=[]
a=999
b=999
while a>100:
	c=str(a*b)
	if c==c[::-1] and int(c) not in palindrome:
		palindrome.append(int(c))
	else:
		if b<100:
			b=a
			a-=1
		else:
			b-=1
palindrome.sort()
print(palindrome[-1])

