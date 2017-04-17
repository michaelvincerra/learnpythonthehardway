class Poem(object):

	def __init__(self, stanza):
		self.stanza = stanza
	
	def tell_me_a_poem(self): 
		for line in self.stanza: 
			print line
	
han_shan3 = Poem(["Look upon the body as unreal,",
					"an image in the mirror,",
					"the reflection of the moon in water.",
					"Contemplate the mind as formless,",
					"Yet bright and pure."])
								
han_shan4 = Poem(["Not a single thought arising", 
					"empty, yet perceptive;",
					"still, yet illuminating;",
					"complete like the great emptiness,",
					"containing all that is wonderful."])
					
han_shan3.tell_me_a_poem()

han_shan4.tell_me_a_poem()


					
	

