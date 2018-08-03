#main.py
#the import section
import webapp2
import jinja2
import os
env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)) #__file__ is current file
    )



#the handler section
class CollectInfo(webapp2.RequestHandler):
    def get(self): #for a GET request
        template = env.get_template("templates/collect_info.html")
        self.response.write(template.render())
class Story(webapp2.RequestHandler):
    def post(self):
        template = env.get_template("templates/story.html")
        correct = self.request.get("number")
        total = self.request.get("largerNumber")
        templateVars = {
            "protagonist": self.request.get("protagonist"),
            "event": self.request.get("event"),
            "pluralNoun": self.request.get("pluralNoun"),
            "name": self.request.get("name"),
            "skill": self.request.get("skill"),
            "number": int(correct/total *100),
            "adjective": self.request.get("adjective"),
            "place": self.request.get("place"),
            "noun": self.request.get("noun")
        }
        self.response.write(template.render(templateVars))

#the app configuration section
app = webapp2.WSGIApplication([
    ('/', CollectInfo),
    ('/story', Story) #this maps the root url to the MainPage Handler
], debug=True)
