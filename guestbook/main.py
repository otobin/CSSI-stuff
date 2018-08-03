import webapp2
import jinja2 # import library defined in app.yaml
import os


import logging
from google.appengine.api import users #new data base--application interface
from google.appengine.ext import ndb

#set up jinja environment
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Message(ndb.Model):
     email = ndb.StringProperty()
     content = ndb.StringProperty()
     created_time = ndb.DateTimeProperty(auto_now_add = True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info("This is the main handler")
        login_url = ""
        logout_url = ""
        current_user = users.get_current_user()
        #the current user will be a user object or none
        #if nobody is logged in, show a login prompt
        if not current_user:
            login_url = users.create_login_url("/")
        else:
            logout_url = users.create_logout_url("/")

        #Read and write from the database:
        message_query = Message.query()
        message_query = message_query.order(-Message.created_time)
        messages = message_query.fetch()
        templateVars = {
            "current_user":  current_user,
            "login_url": login_url,
            "logout_url": logout_url,
            "messages": messages,
        }
        template = env.get_template("templates/guestbook.html")
        self.response.write(template.render(templateVars))
    def post(self):
        #1.) get information from the request
        current_user = users.get_current_user()
        email = current_user.email()
        content = self.request.get("content")
        #2.) Read/write to the database
        message = Message(email = email, content = content)
        #3.) Render a response
        message.put() #saving the content into the database
        self.redirect("/")

app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug = True)
