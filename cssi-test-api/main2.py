import webapp2
import jinja2 # import library defined in app.yaml
import os
import time
import logging
from google.appengine.api import users #new data base--application interface
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
import json

API_KEY = "AIzaSyA7Uo226eyoZjz2H2gQh2eY-pgR5PzbES8"
place_name = "Exploratorium"
url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=%s&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyA7Uo226eyoZjz2H2gQh2eY-pgR5PzbES8" %(place_name)


#set up jinja environment
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# class Person(ndb.Model):
#     name = ndb.StringProperty()
#     biography = ndb.StringProperty()
#     birthday = ndb.DateProperty()
#     email = ndb.StringProperty()

class MainPage(webapp2.RequestHandler):
    def get(self):
        response = urlfetch.fetch(url)
        json_result = json.loads(response.content)
        self.response.write(json_result["candidates"])

app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug = True)
