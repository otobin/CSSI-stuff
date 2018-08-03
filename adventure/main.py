
import webapp2
import jinja2 # import library defined in app.yaml
import os

#set up jinja environment
env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)) #__file__ is current file
    )



class MainPage(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/start.html")
        self.response.write(template.render())

class JumpIn(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/jumpin.html")
        self.response.write(template.render())

class Run(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/run.html")
        self.response.write(template.render())

class Email(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/email.html")
        self.response.write(template.render())

class Ignore(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/ignore.html")
        self.response.write(template.render())

class Accept(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/accept.html")
        self.response.write(template.render())

class Reject(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/reject.html")
        self.response.write(template.render())

class Run(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/run.html")
        self.response.write(template.render())

class PullOver(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/pullover.html")
        self.response.write(template.render())

class Drive(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/drive.html")
        self.response.write(template.render())



app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/run", Run),
    ("/jumpin", JumpIn),
    ("/email", Email),
    ("/ignore", Ignore),
    ("/accept", Accept),
    ("/reject", Reject),
    ("/pullover", PullOver),
    ("/drive", Drive),
], debug = True)
