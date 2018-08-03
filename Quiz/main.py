import webapp2
import jinja2
import os
env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)) #__file__ is current file
    )



#the handler section
class ShowQuiz(webapp2.RequestHandler):
    def get(self): #for a GET request
        template = env.get_template("templates/quiz.html")
        self.response.write(template.render())
class ShowResult(webapp2.RequestHandler):
    def post(self):
        result = self.request.get("question1")
        if result == "val1":
            template = env.get_template("templates/gryffindor.html")
            self.response.write(template.render())
        elif result == "val2":
            template = env.get_template("templates/huffelpuff.html")
            self.response.write(template.render())
        elif result == "val3":
            template = env.get_template("templates/ravenclaw.html")
            self.response.write(template.render())
        elif result == "val4":
            template = env.get_template("templates/slytherin.html")
            self.response.write(template.render())
#the app configuration section
app = webapp2.WSGIApplication([
    ('/', ShowQuiz),
    ('/result', ShowResult) #this maps the root url to the MainPage Handler
], debug=True)
