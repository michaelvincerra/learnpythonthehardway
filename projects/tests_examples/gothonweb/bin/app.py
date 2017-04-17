import web

urls = ('/hello', 'Index')

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')


class Index(object):
	def GET(self):		
		return render.hello_form()
		
		
	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)

		
		##if form.greet:
		#greeting = "%s, %s" % (form.greet, form.name)
		#return render.index(greeting = greeting)
		#else:
		#return "ERROR: greet is required."
		#greeting = "Hello World!"
		#greeting = "This time we call foo!"
		#return render.index(greeting = greeting)
		#return render.foo(greeting = greeting); this is a second option to test another file.
		
		 
if __name__ == "__main__":	
	app.run()


		#note: Previously on Line 13-14: try # commenting out the next line and then refresh browser to see error
		#messages.  Review the "local vars" and 'request information' for guidance.  
		#greeting = "Hello World!"
		#return greeting
