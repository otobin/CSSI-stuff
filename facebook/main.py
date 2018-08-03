import webapp2
import jinja2 # import library defined in app.yaml
import os

from google.appengine.ext import ndb #new data base

#set up jinja environment
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Post(ndb.Model):
    name = ndb.StringProperty()
    message = ndb.StringProperty()
    created_time = ndb.DateTimeProperty(auto_now_add = True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        #2.) REad from or write to the database
        post_query = Post.query()
        post_query= post_query.order(-Post.created_time) #didn't specify an order
        posts = post_query.fetch()
        templateVars = {
            "posts": posts
        }
        #3.) Render a response
        template = env.get_template("/templates/home.html")
        self.response.write(template.render(templateVars))
    def post(self):
        #1.) Get info from the user request
        name = self.request.get("name")
        message = self.request.get("message")
        #2.) Read from or write to the database
        post = Post(name =name, message =message)
        #3.) render a response
        post.put()
        self.redirect("/")


app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug = True)
