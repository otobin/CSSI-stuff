import json
import argparse
import webapp2
import urllib
from google.appengine.api import urlfetch
import jinja2
import os
import logging

API_KEY = "AIzaSyD7TnZoyTqVVjD3_Uy1uB7MLE0j9na6T8o"
url = "https://language.googleapis.com/v1beta2/documents:analyzeSentiment?key=" + API_KEY



env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#print(result["categories"])

class MainPage(webapp2.RequestHandler):
    def get(self):
        def getSentiment(url): #url is unique to sentiment function in api
            data = {
                "document": {
                "type": "PLAIN_TEXT",
                "language": "EN",
                "content": "Google, headquartered in Mountain View, unveiled the new Android phone at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones."
              },
              "encodingType": "UTF32",
            }
            headers = {
            "Content-Type" : "application/json; charset=utf-8"
                }
            jsondata = json.dumps(data)
            result = urlfetch.fetch(url, method=urlfetch.POST, payload=data,headers=headers)
            python_result = json.loads(result.content)
            string = ""
            magnitude = python_result["documentSentiment"]["magnitude"]
            score = python_result["documentSentiment"]["score"]
            if (score < 0.0):
                string = "Your resume has a " + str(score) + " score  and a " + str(magnitude) + " magnitude. This reads as negative"
            elif (score > 0.0 and score < .5):
                string = "Your resume has a " + str(score) + " score  and a " + str(magnitude) + " magnitude. This reads as neutral"
            elif (score > .5):
                string = "Your resume has a " + str(score) + " score  and a " + str(magnitude) + " magnitude. This reads as positive"
            return string
        print(getSentiment(url))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
