

def scan(sentence): 
	verb = ('go', 'stop', 'kill', 'eat')
	direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
	stop = ('the', 'in', 'of', 'from', 'at', 'it')
	noun = ('door', 'bear', 'princess', 'cabinet')
	number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
	#define what function the "()" has below.
	
	
	#lexical_element =  ("go" : "verb", "stop": "verb", "kill" : "verb", "eat": "verb",
						#"north": "direction", "south": "direction", "east": "direction", 
						#"west": "direction", "down" : "direction", "up" : "direction", 
						#"left": "direction", "right" : "direction", "back" : "direction"
						#"stop": "the", "stop": "in", "stop": "of", "stop": "stop": "from", 
						#"stop": "at", "stop" : "it", "door": "noun", "bear": "noun", 
						#"princess": "noun", "cabinet": "noun", "0": "number", "1": "number",
						#"2": "number", "3": "number", "4": "number" , "5": "number", 
						#"6": "number", "7": "number", "8": "number", "9": "number")
						
						
	#word_type = lexical_elements.get(word, 'error')
	
	
	
	#sentence = raw_input('> ')
	word = sentence.split()
	set = []
	
	
	for val in word:
		if val in verb:
			a = ('verb', val)
			set.append(a)
		elif val in direction:
			a = ('direction', val)
			set.append(a)
		elif val in stop:
			a = ('stop', val)
			set.append(a)
		elif val in noun:
			a = ('noun', val)
			set.append(a)
		else:
			try: 
				num = int(val)
				a = ('number', num)
				set.append(a)
			#write into the following a way to handle 'error'. 
			except ValueError:
				a = ('error', val)
				set.append(a)
				
	return set
		
	