#Project Euler 1
#19/08/13

#"If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000."

#Initial longer solution
# multiples=[]
# for i in range(0,1000):
# 	if i%3==0 or i%5==0 and i not in multiples:
# 		multiples.append(i)
# print(sum(multiples))



#Second shorter lambda solution
print(sum(i for i in range(1, 1000) if i%3==0 or i%5==0))
