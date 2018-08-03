import webapp2
import jinja2 # import library defined in app.yaml
import os
import time
import logging
from google.appengine.api import users #new data base--application interface
from google.appengine.ext import ndb






#set up jinja environment
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Person(ndb.Model):
    name = ndb.StringProperty()
    biography = ndb.StringProperty()
    birthday = ndb.DateProperty()
    email = ndb.StringProperty()

class MainPage(webapp2.RequestHandler):
    def get(self):
        current_user = users.get_current_user()
        if current_user:
            current_email = current_user.email()
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None
        logout_url = users.create_logout_url("/")
        login_url = users.create_login_url("/")
        #Read the request

        #Read and write from the database
        people = Person.query().fetch()
        templateVars = {
            "people": people,
            "current_user": current_user,
            "login_url": login_url,
            "logout_url": logout_url,
            "current_person": current_person,
        }
        template = env.get_template("/templates/home.html")
        self.response.write(template.render(templateVars))
    def post(self):
        name = self.request.get("name")
        biography = self.request.get("bio")
        current_user = users.get_current_user()
        email = current_user.email()
        person = Person(name = name, biography = biography, email = email)
        person.put()
        time.sleep(2)
        self.redirect("/")
class Profile(webapp2.RequestHandler):
    def get(self):
        #Get information from the database
        urlsafe_key = self.request.get("key")
        logging.info(urlsafe_key)
        #Read or write from the database
        key = ndb.Key(urlsafe = urlsafe_key)
        person = key.get()
        templateVars = {
            "person": person
        }
        #Render a response
        template = env.get_template("/templates/profile.html")
        self.response.write(template.render(templateVars))



app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/profile", Profile),
], debug = True)
