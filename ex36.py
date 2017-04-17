# write a game exercise, based on ex35.py
from sys import exit

def A_room():
	print "You can inherit some of Pablo Picasso's financial estate. How many dollars $ do you take?"
	# I'm not clear on how below works. Figure it out!

	choice = raw_input("> ")
	if  "0" in choice or "1" in choice: 
		how_much = int(choice)
	else: 
		dead("Learn to be stealthy, and then wealthy!")
	
	if how_much >500:
		print "Awesome! Now you know that Cubism and Relativity are related!" 
		exit(0)
	else:
		dead("Each cubic inch of your intelligence is neither artistic nor scientific.")
	
def B_room():
	print "You encounter Albert Einstein, the greatest Scientist, but he has amnesia."	
	print "You forget the Theory of Relativity."	
	print "You remember Quantam Mechanics."	
	print "Do you explain that light and matter is made up of waves, particles, or wave-particles, or none of the above?"	
	einstein_laughs = False
	
	while True: 
		choice = raw_input("> ")
	
		if choice == "waves":
			dead("Einstein recommends that you return to study Quantum Mechanics again.")	
		elif choice == "wave-particles." and not einstein_laughs:
			print "Congratulations.  Enter the black hole through the manhole cover." 
			einstein_laughs = True
		elif choice == "particles":
			dead("Einstein deflects your question and asks you to read Richard Feynman.")		
		elif choice == "None of the above" and einstein_laughs:
			A_room()
		# review the following function to assure that 'and' can be used, else and	
		else:
			print "I've got no idea about Science!" 

def C_room():
	print "You encounter Frankenstien"
	print "Frankenstein was electrocuted and is chained to 24OV cabinet, suffering." 
	print "Do you kills or save Frankenstein?"
	
	choice = raw_input("> ")
	
	if "save" in choice:
		start()		
	elif "kill" in choice:
		dead("That was not wise, my friend. You die too.")	
	else: 
		C_room

def dead(why):
	print why, "Your still brilliant!"
	exit(0)	
		
def start():
	print "You're given a grant of $10,000 to study Python and Javascript."
	print "Decide which field where you'll contribute innovation."
	print "Do you choose Art or Science?"
	
	choice = raw_input("> ")	
	
	if choice == "Art":
		A_room()
	elif choice == "Science":
		B_room()	
	else:
		dead("Game over.")
		
start()
			

	
	
	