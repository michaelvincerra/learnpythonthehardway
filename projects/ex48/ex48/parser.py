class ParserError(Exception):
	pass

class Sentence(object):
    def __init__(self, subject, verb, object):
        """ Each argument 'subject', 'verb', 'object' is a tuple containing the code and word"""
        self.subject = subject
        self.verb = verb
        self.object = object

def peek(word_list):
    """ 
    word_list is a list of tuples in the form (code, word).
    This method returns the code of the first tuple in the list
    """
    if(word_list):
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    """ 
    Returns the first word if it matches the expecting type, else returns None.
    In any case, the first word will be removed from the word_list
    """
    ret_val = None
    if(word_list):
        word_tuple = word_list.pop(0)
        if(word_tuple[0] == expecting):
            ret_val =  word_tuple
    
    return ret_val

def skip(word_list, word_type):
    if(word_list):
        while(peek(word_list) == word_type):
            match(word_list, word_type)

def parse_subject(word_list, subject):
    skip(word_list, 'stop')
    verb = match(word_list, 'verb')
    if(verb == None):
        raise ParseError("Expecting a verb")

    skip(word_list, 'stop')
    object = match(word_list, 'noun')
    if(object == None):
        raise ParseError("Expecting a noun")

    return Sentence(subject, verb, object)

def parse_sentence(word_list):
    """ Accepts a list of tuples, where each tuple contains (code, word)"""
    skip(word_list, 'stop')
    start = peek(word_list)
    if(start == 'noun'):
        subject = match(word_list, 'noun')
        return parse_subject(word_list, subject)
    elif(start == 'verb'):
        subject = ('noun', 'player')
        return parse_subject(word_list, subject)
    else:
        raise ParseError("Must start with either a noun or a verb ... not '%s'" % start)
    

	
#class Sentence(object): 
#	def __init__(self, subject, verb, obj): 
	#remember we take ('noun', 'princess') tuples and convert them
	#from self get subject and set it to subject[1]
#		self.subject = subject[1]
	#	from self get verb and set it to verb[1]
#		self.verb = verb[1]
	#	from self get object and set it to obj[1]
#		self.object = obj[1]

		
#	def to_tuple(self):
#		return (self.subject, self.verb, self.object)
		
# what is word_list? Where is it defined? 	
#	def peek(word_list):
#		if word_list: 
#			word  = word_list[0]
#			return word[0]			
#		else:
#			return None		
			
#	def match(word_list, expecting):
#		if word_list:
		#what is the .pop() function doing? 
		#pop()Remove and return an arbitrary element from the set. 
		#Raises KeyError if the set is empty.
#			word = word_list.pop(0)
			
#			if word[0] == expecting:
#				return word
#			else:
#				return None
#		else:
#			return None
	
#	def skip(word_list, word_type):
#		while peek(word_list) ==  word_type:
#			match(word_list, word_type)
			
#	def parse_verb(word_list):
#		skip(word_list, 'stop')
		
#		if peek(word_list) == 'verb':
#			return match(word_list, 'verb')
#		else: 
#			raise ParserError("Expected a verb next.") 
			
#	def parse_object(word_list):
#		skip(word_list, 'stop')
#		next_word = peek(word_list)
		
#		if next_word == 'noun':
#			return match(word_list, 'noun')
#		elif next_word == 'direction':
#			return match(word_list, 'direction')
#		else: 
#			raise ParserError("Expected a noun or direction next.")

#	def parse_subject(word_list, subject):
#		skip(word_list, 'stop')
#		next_word = peek(word_list)
		
#		if next_word =='noun':
#			return match(word_list, 'noun')
#		elif next_word =='verb':
#			return ('noun', 'player')
#		else:
#			raise ParserError("Expected a verb next.")
			
		
		
#		verb = parse_verb(word_list)
#		object = parse_object(word_list)
		
#		return Sentence(subject, verb, object)	
		
		#skip(word_list, 'stop')
		#next_word = peek(word_list)	
		#if next_word == 'noun': 
		#	return match(word_list, 'noun')
		#elif next_word == 'verb': 
		#	return ('noun', 'player')
		#else: 
		#	raise ParserError("Expected a verb next.")
		
		#return Sentence(subject, verb, object)		

		
			
	 
#	def parse_sentence(word_list):
#		subj = parse_subject(word_list)
#		verb = parse_verb(word_list)
#		obj = parse_object(word_list)
	
#		return Sentence(subj, verb, obj)
		
		#alternative method
		
#def parse_sentence(word_list):
 #   skip(word_list, 'stop')

  # start = peek(word_list)
#	if start == 'noun':
#        subj = match(word_list, 'noun')
#        return parse_subject(word_list, subj)
#    elif start == 'verb':
#        return parse_subject(word_list, ('noun', 'player'))
#    else:
#        raise ParserError("Must start with noun or verb, not: %s" % start)
	
	
	##def Sentence(subject):
	##	for subject in verb
	##	...
		
	##def Sentence(verb): 
	##	for verb in ...
		
	##ef SentenceI(object): 
	##	for object in ...
		
		
	