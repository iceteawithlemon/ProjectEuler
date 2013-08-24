# Project Euler
# 24/08/13

#brute force
n=100
E1=0
E2=0
for i in range(0, n+1):
	E1+=i**2
	E2+=i
E2=E2**2
print(E2-E1)

#according to solution
n=100
E1=(n*(n+1)/2)**2
E2=(2*n+1)*(n+1)*n/6
print(E1-E2)