import jinja2
import os
import webapp2

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)) #__file__ is current file
    )

#the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a GET request
        template = env.get_template("/templates/home.html")
        self.response.write(template.render())


class SignUp(webapp2.RequestHandler):
    def post(self):
        age = int(self.request.get("age")) #get all lets you select multiple
        templateVars = {
            "username": self.request.get("username"),
            "password": self.request.get("password"),
            "tier": self.request.get("tier"),
            "legal": age > 13,
            "newsletter": bool(self.request.get("newsletter")),
        }
        template = env.get_template("/templates/signup.html")
        self.response.write(template.render(templateVars))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ("/signup", SignUp) #this maps the root url to the MainPage Handler
], debug=True)
