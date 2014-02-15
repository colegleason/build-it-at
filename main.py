import os
import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from handlers.handlers import handlers

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

application = webapp2.WSGIApplication(handlers, debug=True)
