# build and return a list
# look up this lesson: https://wiki.python.org/moin/Generators

def firstn(): 
	# what function does the "[]" serve
	num = 0
	while num < n:
		yield  num
		num += 1
	
sum_of_first_n = sum (firstn(1000000))
	
	