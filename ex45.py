# write a game exercise, based on ex35.py
from sys import exit

n = [0,1,2,3,4,5,6,7,8,9] 
#restart here with more classes. How do art, science, electronics become part of "Rooms"? 


class Rooms(object): 
	
	
	def __init__(self): 
		#self.counter is set to false; therefore, when self.counter, below, is set to: 
		#self.counter =1, the second time the loop is run, 0 != 1, and the else condition
		#is executed. 
		# self.counter is called an "attribute."
		self.counter = 0	

	def art(self):
	
	 	print "You inherit some of Pablo Picasso's financial estate." 
	 	print "How many $ millions of dollars do you take?"
		print "Will you exceed the number given?" 

		#if "<9" in choice: 
		#	n = int(choice)
	
		#if  "0" in choice or "1" in choice: 
		#	how_much = int(choice)
		#else: 
		
		# NOTE: Per Kieran, in case where you use a complicated while loop, like the one
		#below, typically this while loop is stored as a separate file. 
		#Then, that file is imported into this main file. 
		# And, Python developers like to have separated: Objects & Classes; While loops; and basic function methods. 
		
		
		
		while True: #infinite loop
			# Note: the variable at right must be preceded by "int" which dictates that it be a "number" or integer. 
			choice = int(raw_input(">Input a number between 0-9: "))
			#If the counter is set to "0", then the first time the script hits self.counter = 1, it will abort
			# because the variable is set to "0" or False. 
			self.counter = 0	
	 	
			#length = len(choice)
			#max_char = 1
			#for i in choice:
			print "%s million!" % choice
			
			if choice == 0 or choice == 1 or choice == 2 or choice == 3: 
				print "You should have taken more! Making art is expensive!"
				break
 			elif choice == 4 or choice == 5 or choice == 6:
 				print "Quit your job. Purchase your first studio, and get to work!"
 				print "The Python Grant of $10,000 is yours!"
 				break
			elif choice == 7 or choice == 8:
				print "You greedy bastard!!! Leave $ for other starving artists."
				#continue
			elif choice >= 9 and self.counter == 0:
				print "Are you reading directions? Here's one more chance." 
				return self.art()
				self.counter = 1				
			#elif choice not in n:
			#	print dead
			#	break
			else: 
				self.dead("First learn to be stealthy, then wealthy!")
				break
			#you're increasing the run-time without any benefit if you un-indent "break".  
			
			#elif choice.__contains__(n): 
			#for choice in range(0,3):
			#if  choice == n[0] or choice == n[1] or choice == n[2] or choice == n[3]: 
			
			#if  any(number for number in choice <3): 	
			#	print "You should have taken more! Making art is expensive!"
			#elif any(n >3 and <6 in choice):
			#	print "Quit your job. Purchase your first studio, and get to work!"
					
			##if choice in n == "0","1","2","3": 
				##choice == ">0" and "<3"
			#elif choice == n[4] or choice == n[5] or choice == n[6]:
			#">3" and "<5" in choice:		
			#choice in n == "0","1","2","3":
				##choice == ">3" and "<5"
#				print "Quit your job. Purchase your first studio, and get to work!"
			#elif choice == n[7] or choice == n[8] or choice == n[9]: 
				#">5" and "<9" in choice:  
				#choice in n:
				#choice == ">5" and "<9"
			#	print "You're a greedy bastard! Leave $ for other starving artists."
			

		#	print n		
		#if n in n():
				#	return n
	
		#if n == 1: 
		#	how_much = choice
		#else: 			
		#	how_much = -1 
		
		#range(-1, 10):
		#while True:
		#	if n in  n:
		#		return n
		#	n = choice()
						
		#else: 
		#	self.dead("Learn to be stealthy, then wealthy!")
	
		#if how_much >5:
		#	print "Awesome! Now you know Cubism and The General Theory Relativity are related!" 
		#	exit(0)
		#else:
		#	dead("You're neither artistic nor scientific. Go back to school!")
	
	def science(self):
		print "You encounter Albert Einstein, but he has amnesia."	
		print "You must explain how Physics evolved since the General Theory of Relativity."	
		print "You cannot use any part of Quantam Mechanics."	
		print "Do you explain light and matter is made of: waves, particles, or wave-particles, or none of the above?"	
		einstein_laughs = True
		
		
		while True: 
			# the following raw_input defaults to a string. 
			# Remember: "Strings are iterable and sequential; integers are not." Kieran
			choice = raw_input("Type exact word> ")
	
			if choice == "waves":
				self.dead("Einstein recommends that you return to study his Theory of Relativity.")	
			elif choice == "wave-particles":
				print "Congratulations! Enter the black hole through the manhole cover." 
				print "The Python Grant of $10,000 is yours!"
				break
			elif choice == "particles":
				self.dead("Einstein deflects your question and asks you to read Richard Feynman.")		
			elif choice == "none of the above" and einstein_laughs:
				print "Goodbye!"
				break
			# review the following function to assure that 'and' can be used, else and	
			else:
				print "You've got no idea about science! Einstein laughs!!!"  
				break

	def electronics(self):
		print "You encounter Frankenstien"
		print "Frankenstien was electrocuted but still alive, chained to 24OV cabinet, suffering." 
		print "Do you 'save' or 'kill' Frankenstien?"
	
		choice = raw_input("Type exact word> ")
	
		if "save" in choice:
			print "You win the Python Grant of $10,000!"	
		elif "kill" in choice:
			self.dead("That was not wise, my friend. You die too.")	
		else: 
			self.dead("Learn compassion, my friend.")

	def dead(self, why):
		print why, "You're banished from using the Python Grant!"
		exit(0)	
		
	def start(self):
		print "You're given a chance to win a Python Grant of $10,000."
		print "First, you must pass a test to use money for an altruistic goal." 
		print "In which field will you contribute Python knowledge?: art, science, or electronics"
	
		choice = raw_input("Type exact name> ")	
	
		if choice == "art":
			self.art()
		elif choice == "science":
			self.science()
		elif choice == "electronics":
			self.electronics()	
		else:
			self.dead("You're dead.")

dead = "Game Over. Your greed exceeds your need."
game = Rooms()		
game.start()
			
	#if  "0" in choice or "1" in choice: 
		#how_much = int(choice)
		
		#review this section carefully
	
	
	