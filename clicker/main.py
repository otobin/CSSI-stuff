import webapp2
import jinja2 # import library defined in app.yaml
import os


from google.appengine.ext import ndb

#set up jinja environment
env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)) #__file__ is current file
    )

class ClickCounter(ndb.Model):
    clicks = ndb.IntegerProperty()

class MainPage(webapp2.RequestHandler):
    def get(self):
        click_counter = ClickCounter.query().get() #give me all models that are type ClickCounter
        #check if its the first click
        if not click_counter: #if click counter is empty
            click_counter = ClickCounter(clicks=0)
        templateVars = {
            "click_count": click_counter.clicks,
        }
        template = env.get_template("/templates/clicky.html")
        self.response.write(template.render(templateVars))
    def post(self):
        click_counter = ClickCounter.query().get() #give me all models that are type ClickCounter
        #check if its the first click
        if not click_counter: #if click counter is empty
            click_counter = ClickCounter(clicks=0)
        click_counter.clicks += 1
        click_counter.put() #updated value of clicks-->saves
        templateVars = {
            "click_count": click_counter.clicks, #saves value of clicks into template vars
        }
        template = env.get_template("templates/clicky.html")
        self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ("/", MainPage),

], debug = True)
