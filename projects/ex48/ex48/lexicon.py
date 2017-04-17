class lexicon(object):
	def __init__(self):
        # TODO: Can we make these as constants so they can be accessed from out side the class with just the class name ?
        self.C_DIRECTION_WORDS = "direction"
        self.C_VERBS = "verb"
        self.C_STOP_WORDS = "stop"
        self.C_NOUNS = "noun"
        self.C_NUMBER = "number"
        self.C_ERROR = "error"

        #lexicon
        self.direction_words = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
        self.verbs = ['go', 'stop', 'kill', 'eat']
        self.stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
        self.nouns = ['door', 'bear', 'princess', 'cabinet']
        
    def get_tuple(self, word):
        ret_val = None
        lword = word.lower()
        if(lword in self.direction_words):
            ret_val = (self.C_DIRECTION_WORDS, word)
        elif(lword in self.verbs):
            ret_val = (self.C_VERBS, word)
        elif(lword in self.stop_words):
            ret_val = (self.C_STOP_WORDS, word)
        elif(lword in self.nouns):
            ret_val = (self.C_NOUNS, word)
        elif(self.convert_number(lword) != None):
            ret_val = (self.C_NUMBER, self.convert_number(lword))
        else:
            ret_val = (self.C_ERROR, word)

        return ret_val

    def convert_number(self, text):
        try:
            return int(text)
        except ValueError:
            return None


def scan(line):
    the_lexicon = lexicon()
    ret_val = []
    words = line.split()
    for word in words:
        the_tuple = the_lexicon.get_tuple(word)
        ret_val.append(the_tuple)

    return ret_val

##def scan(sentence): 
##	#following are the tuples
##	verb = ('go', 'stop', 'kill', 'eat')
##	direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
#	stop = ('the', 'in', 'of', 'from', 'at', 'it')
#	noun = ('player' 'door', 'bear', 'princess', 'cabinet')
#	number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
#	#define what function the "()" has below.
	
	
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
	
	

#def convert_number(s):
#   try:
#        return int(s)
#   except ValueError:
#        return None

#def scan(strInput):
#    wordList = strInput.lower().split(' ')
#    resultSentence = []

#    for word in wordList:
#        if word in direction:
#            resultSentence.append(('direction', word))
#        elif word in verb:
#            resultSentence.append(('verb', word))
#        elif word in stop:
#            resultSentence.append(('stop', word))
#        elif word in noun:
#            resultSentence.append(('noun', word))
#        elif convert_number(word) is not None:
#            resultSentence.append(('number', int(word)))
#        else:
#            resultSentence.append(('error', word))

#    return resultSentence
	
	
#def scan(strInput):	
#	wordlist = strInput().sentence.split()
#	sentence_result = []
	#changed 'val' to 'word' below
	
#	for word in wordlist:
#		if word in verb:
#			a = ('verb', word)
#			sentence_result.append(a)
#		elif word in direction:
#			a = ('direction', word)
#			sentence_result.append(a)
#		elif word in stop:
#			a = ('stop', word)
#			sentence_result.append(a)
#		elif word in noun:
#			a = ('noun', word)
#			sentence_result.append(a)
#		else:
#			try: 
#				num = int(word)
#				a = ('number', num)
#				sentence_result.append(a)
			#write into the following a way to handle 'error'. 
#			except ValueError:
#				a = ('error', word)
#				sentence_result.append(a)
				
#	return sentence_result
		
	