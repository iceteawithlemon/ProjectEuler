#Project Euler 5
#20/08/13

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 20# = 2 10 4 5
# 19
# 18# = 2 9 3 6
# 17
# 16# = 2 8 4
# 15# = 3 5
# 14# = 2 7
# 13
# 12# = 2 6 3 4
# 11
# # 10 = 2 5
# # 9 = 3
# # 8 = 2 4
# # 7
# # 6 = 2 3
# # 5
# # 4 = 2
# # 3
# # 2
# # 1
#This tells us that if a number is divisible by all the numbers between 11 and 20, then it is also divisible by all the numbers between 1 and 10.
# alist=[]
# alist2=[]
# a=20*19*18*17*16*15*14*13*12*11
# aes=[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
# a=6*7*8*9*10
# aes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i=0
# while input("Carry on? (y) ")=='y':
# 	while i<len(aes)-1:
# 		print("aes[i]", aes[i], i)
# 		while a%aes[i+1]==0 and a not in alist:
# 			a/=aes[i]
# 			alist.append(a)
# 			i=0
# 		i+=1
# 	print(alist)
# 	for c in alist:
# 		for b in range(1, 21):
# 			alist2.append(c/b)
# 	print(alist2)

#We know the 2520 is the smallest number that can be divided by all the numbers from 1 to 10, and if a number can be divided by 11-20 then it can by 1-10
#So the answer must be a multiple of 2520
i=0
mlist=[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
a=2520
foundIt=False
x=20
while not foundIt:
	while i in range(0, len(mlist)):
		x-=1
		if a%mlist[i]!=0:
			a+=2520
			i=0
			break
		elif a%mlist[i]==0:
			i+=1
	if i==len(mlist):
		print(a)
		foundIt=True
		break
