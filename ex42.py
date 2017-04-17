## This exercise is ALL ABOUT learning INHERITANCE. See Comments in parentheses. 
## See: http://stackoverflow.com/questions/6976988/learn-python-the-hard-way-2nd-edition-exercise-45
## "Everything you can bind to a name in Python is an object. Even classes are objects."
## Animal is-a object (yes, sort of confusing) look at the extra credit.
class Animal(object):
	pass
	
## Dog is-a Animal (Animal is-a Object, so Dog is-a Object too -INHERITANCE!)
class Dog (Animal):

	def __init__(self, name):
	
		self.name = name
		
## Cat is-a Animal 
# Animal is-a Object, so Cat is-a Object too.
# class Cat is-a Animal that has-a __init__that takes self and name parameters 
class Cat(Animal):
	def __init__(self, name):
		## from self get name and set to name
		self.name = name
		
## Person is-a object
## that has-a __init__that takes self and name parameters.
class Person(object):

	def __init__(self, name):
		## self has-a name
		## from self, get name and set it to name. 
		self.name = name
		
		## self has-a pet that is SET to None
		## from self, get pet and set it to None
		self.pet = None
		
## Employee is-a Person
class Employee(Person):
	def __init__(self, name, salary): 
		## has-a
		super(Employee, self).__init__(name)
		## has-a
		self.salary = salary
		
## Fish is-a Object
class Fish(object): 
	pass
	
## Salmon is-a Fish
class Salmon(Fish):
	pass
	
## Halibut is-a Fish	
class Halibut(Fish): 

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet named Satan
mary.pet = satan


## frank is-a Employee
## frank is-a Person because of Line 35 "class Employee(Person):"
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## Flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

