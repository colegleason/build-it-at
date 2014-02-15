import webapp2

class NewIdea(webapp2.RequestHandler):
    def get(self):
        self.response.write('New idea')
