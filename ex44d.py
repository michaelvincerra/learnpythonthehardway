class Parent(object): 
#The concept that one class can inherit traits from another class, much like you and your parents.

#class Parent has a function named override that takes self parameters
	def override(self): 
		print "PARENT override()"

#class Parent has a function named implicit that takes self parameters		
	def implicit(self):
		print "PARENT implicit()"
		
#class Parent has a function named altered that takes self parameters	
	def altered(self):
		print "PARENT altered()" 
		
#Child is-a Parent, which is to say that it inherits from the Parent		
class Child(Parent): 

#class Child has a function named override that takes self parameters
	def override(self):
		print "CHILD override()"
		
#class Child has a function named altered that takes self parameters		
	def altered(self): 
		print "CHILD, BEFORE PARENT altered()"
# In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable.	
# super method calls __init__ method from Class Parent instead of Child. It redirects to the Parent object. 
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"


#Set dad to an instance of Parent			
dad = Parent()

#Set son to an instance of Child
son = Child()

# from dad get implicit	
dad.implicit()
# from son get implicit
son.implicit()

#from dad get override
dad.override()
#from son get override
son.override()

#from dad get altered
dad.altered()
#from son get altered
son.altered()
	
		