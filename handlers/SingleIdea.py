import webapp2

class SingleIdea(webapp2.RequestHandler):
    def get(self, idea_id):
        template_values = {
           'ideas': ideas,
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
