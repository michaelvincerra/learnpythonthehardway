# following are all stored lists, this uses FOR LOOPS
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
# following is a mixed list
change = [1, 'pennies', 2,'dimes', 3, 'quarters']
art = [ 'painting', 'sculpture', 'printmaking', 'performance art', 'design']

#this first kind of for-loop goes through a list 
for number in the_count:
	print "This is count %d" % number
	
# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
#also we can go through the mixed lists too
#notice we have to use %r since we don't know what's in it.
for i in change:
	print "I got %r" % i
	
for art in art: 
	print "A type of art such as: %s" % art	
	
#I added this example to try to understand the purpose of "i" -- no reggae pun unintended
elements = []	

for i in range (0,10):
	print "Adding more  %d to the list." % i
	elements.append(i)
	
	
#we can also build lists, first start with an empty one
# UNDERSTAND HOW THE EMPTY ELEMENT COMMAND WORKS!!!
elements = []	

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	#append is a function that lists understand
	elements.append(i)
	
#now we can print them out too
for i in elements:
	print "Element was: %d" % i