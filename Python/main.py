import webapp2
import jinja2 # import library defined in app.yaml
import os

#set up jinja environment
env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)) #__file__ is current file
    )

class MainPage(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name")
        location = self.request.get("location")
        template = env.get_template("templates/profile.html")
        templateVars = { #dictionary
            "name": name,
            "location": location
        }
        self.response.write(template.render(templateVars))

class Friends(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/friends.html")
        self.response.write(template.render())

class Skills(webapp2.RequestHandler):
    def get(self):
        pass
        #skills and other stuff


#can delete later no problem
class Students(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/students.html")
        templateVars = {
            "location": "MTV",
            "students": ["Jackelen", "Savion", "Olivia", "Anyka"]
        }
        self.response.write(template.render(templateVars))


app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/friends", Friends),
    ("/skills", Skills),
    ("/students", Students)
], debug = True)
