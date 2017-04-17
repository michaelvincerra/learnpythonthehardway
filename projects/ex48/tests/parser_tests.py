
from nose.tools import *
from ex48 import parser
from ex48 import lexicon
# a test might look like this

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_peek():
    #test a line with one word
    line1 = "princess"
    word_tuples1 = lexicon.scan(line1)
    word_type1 = sentence.peek(word_tuples1)
    assert_equal("noun", word_type1)

    #test a line with multiple words
    line2 = "princess ate the bear"
    word_tuples2 = lexicon.scan(line2)
    assert_equal("noun", sentence.peek(word_tuples2))

def test_match():
    #test a line with one word
    line1 = "princess"
    word_tuples1 = lexicon.scan(line1)
    assert_equal("princess", sentence.match(word_tuples1, 'noun')[1])
    #Here we should get a None for any type since there is nothing in the word_list
    assert_equal(None, sentence.match(word_tuples1, 'noun'))

    #test a line with multiple words
    line2 = "princess eat the bear"
    word_tuples2 = lexicon.scan(line2)
    assert_equals(4, len(word_tuples2))
    assert_equal("princess", sentence.match(word_tuples2, "noun")[1])
    assert_equal("eat", sentence.match(word_tuples2, "verb")[1])
    assert_equal("the", sentence.match(word_tuples2, 'stop')[1])
    assert_equal("bear", sentence.match(word_tuples2, 'noun')[1])

def test_skip():
    #test a line with one word
    line1 = "princess"
    word_tuples1 = lexicon.scan(line1)
    sentence.skip(word_tuples1, "verb")
    assert_equal(1, len(word_tuples1))
    sentence.skip(word_tuples1, 'noun')
    assert_equal(0, len(word_tuples1))

    #test a line with multiple words
    line2 = "princess eat the bear"
    word_tuples2 = lexicon.scan(line2)
    sentence.skip(word_tuples2, "verb")
    assert_equal(4, len(word_tuples2))
    sentence.skip(word_tuples2, "noun")
    assert_equal(3, len(word_tuples2))
    sentence.skip(word_tuples2, "verb")
    assert_equal(2, len(word_tuples2))
    
    
        

def test_parse_sentence():
    line = "princess eat the bear"
    word_list = lexicon.scan(line)
    parsed_sentence = sentence.parse_sentence(word_list)
    assert_equal("princess", parsed_sentence.subject[1])
    assert_equal("eat", parsed_sentence.verb[1])
    assert_equal("bear", parsed_sentence.object[1])




    
#def test_parse_sentence():
#    s = parser.Sentence(('noun', 'bear'), ('verb', 'eat'),('number', 1), ('noun', 'door'))
#    assert_equal(s.subject, 'bear')
#    assert_equal(s.verb, 'eat')
#    assert_equal(s.object, 'door')
#    assert_equal(s.to_tuple(), ('bear','eat', 1, 'door'))
    
    
    #assert_equal(parser.parse_sentence("1234"), [('number', 1234)])
    #result = parser.scan("3 91234")
    #assert_equal(result, [('number', 3),
       #                   ('number', 91234)])

#def test_parse_subject(): 
#	word_list = lexicon.scan('eat door') 
#	subject = ('noun', 'bear')
#	s = parser.parse_subject(word_list, 'subject')
#  	assert_equal(s.to_tuple(), ('bear','eat', 1, 'door'))    

#def test_peek():
 #   assert_equal(parser.peek("north"), [('direction', 'north')])
    #result = parser.scan("north south east")
    #assert_equal(result, [('direction', 'north'),
        #                  ('direction', 'south'),
        #                  ('direction', 'east')])                       

#def test_match():
    #assert_equal(parser.match("go"), [('verb', 'go')])
    #result = parser.scan("go kill eat")
    #assert_equal(result, [('verb', 'go'),
        #                  ('verb', 'kill'),
        #                 ('verb', 'eat')])


#def test_skip():
    #assert_equal(parser.skip("the"), [('stop', 'the')])
    #result = parser.scan("the in of")
    #assert_equal(result, [('stop', 'the'),
        #                  ('stop', 'in'),
        #                 ('stop', 'of')])


#def test_parse_subject():
    #assert_equal(parser.parse_subject("1234"), [('number', 1234)])
    #result = parser.scan("3 91234")
    #assert_equal(result, [('number', 3),
       #                   ('number', 91234)])






##def test_peek():
    #assert_equal(parser.peek("word_list"), [('word', 'verb', 'obj')])
    #result = parser.scan("word")
    #assert_equal(result, [('word_list', 'subj'),
    #						('word_list', 'verb'), 
    #						('word_list', 'obj')])
	


#def test_parse_verb():
    #assert_equal(parser.parse_verb("bear"), [('noun', 'bear')])
    #result = parser.scan("bear princess")
    #assert_equal(result, [('noun', 'bear'),
#                         ('noun', 'princess')])

#def test_parse_object():
    #assert_equal(parser.parse_object("1234"), [('number', 1234)])
    #result = parser.scan("3 91234")
    #assert_equal(result, [('number', 3),
       #                   ('number', 91234)])




#def test_ParseError():
    #assert_equal(parser.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    #result = parser.scan("bear IAS princess")
    #assert_equal(result, [('noun', 'bear'),
     #                     ('error', 'IAS'),
      #                    ('noun', 'princess')])
      
      