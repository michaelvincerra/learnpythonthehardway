import web
from gothonweb import map

urls = ('/game', 'GameEngine','/', 'Index',)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
                                  initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session

#render = web.template.render('templates/', base="layout")
render = web.template.render('C:/lpthw/gothonweb/bin/templates', base="layout")

class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        session.room = map.START
        web.seeother("/game")


class GameEngine(object):



def GET(self):
    if session.room:
      return render.show_room(room=session.room)
    else:
       return render.you_died()

    def POST(self):
   
        # there is a bug here, can you fix it?
      	if session.room and form.action:
    	 	session.room = session.room.go(form.action)
			#try: session['room']
        web.seeother("/game")

if __name__ == "__main__":
    app.run() 