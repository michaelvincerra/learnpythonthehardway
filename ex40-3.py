class Poem(object):

	def __init__(self, stanza):
		self.stanza = stanza
	
	def tell_me_a_poem(self): 
		for line in self.stanza: 
			print line
	
han_shan1 = Poem(["You find a flower half-buried in leaves",
					"And in your eye its very fate resides.",
					"Loving beauty, you caress the bloom;",
					"Soon enough, you'll sweep petals from the floor."])
								
han_shan2 = Poem(["Terrible to love the lovely so,"
					"To count your own years, to say 'I'm old'",
					"To see a flower half-buried in leaves",
					"And come face to face with what you are."])
					
han_shan1.tell_me_a_poem()

han_shan2.tell_me_a_poem()


					
	

