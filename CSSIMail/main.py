#main.py
#the import section
import webapp2
import jinja2
import os


env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))

)


class Email(object):
    def __init__(self, subject, sender, content, image):
        self.subject = subject
        self.sender = sender
        self.content = content
        self.image = image



#the handler section
class ListEmails(webapp2.RequestHandler):
    def get(self): #for a GET request
        subject = self.request.get("subject")
        sender = self.request.get("sender")
        content = self.request.get("content")
        image = self.request.get("image")
        template = env.get_template("templates/list_emails.html")
        templateVars = {
            "subject": subject,
            "sender": sender,
            "content": content,
            "image": image,
        }
        self.response.write(template.render(templateVars)) #the response



#the handler section
class ViewEmails(webapp2.RequestHandler):
    def get(self): #for a GET request
        template = env.get_template("templates/view_emails.html")
        subject = self.request.get("subject")
        sender = self.request.get("sender")
        content = self.request.get("content")
        image = self.request.get("image")
        templateVars = {
            "subject": subject,
            "sender": sender,
            "content": content,
            "image": image,
        }
        self.response.write(template.render(templateVars)) #the response

#the app configuration section
app = webapp2.WSGIApplication([
    ('/', ListEmails),
    ("/view", ViewEmails) #this maps the root url to the MainPage Handler
], debug=True)
