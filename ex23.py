#https://github.com/tarttelin/Python-Stub-Server | Use: pip install stubserver

from unittest import TestCase
from stubserver import Stubserver

class WebTest(TestCase): 

	def setUp(self)
		self.server = StubServer (8998)
		self.server.run()
	
	#implicitly calls verify on stop		
	def tearDown(self):
		self.server.stop()

	def test_put_with_capture(self):
		capture = {}
		self.server.expect(method="PUT", url="/address?/\d+$, data_capture=capture)\
				   .and_return(reply_code=201)
				   
		#do stuff here
		captured = eval(capture["body"])
		self.assertEquals("world", captured["hello"])