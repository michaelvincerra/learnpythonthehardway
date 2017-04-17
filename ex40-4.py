class Poem(object):

	def __init__(self, stanza):
		self.stanza = stanza
	
	def tell_me_a_poem(self): 
		for line in self.stanza: 
			print line
	
han_shan3 = Poem(["People ask the way to Cold Mountain.",
					"Cold Mountain? There is no road that goes through.",
					"Even in summer the ice doesn't melt;",
					"Though the sum comes out, the fog is blinding."])
								
han_shan4 = Poem(["How can you hope to get there by aping me?", 
					"Your heart and mine are not alike.",
					"If your heart were the same as mine",
					"Then you could journey to the very center!"])
					
han_shan3.tell_me_a_poem()

han_shan4.tell_me_a_poem()


					
	

