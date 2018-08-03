import json
import argparse
import webapp2
import urllib
from google.appengine.api import urlfetch
from google.cloud import language
from google.cloud.language import enums

API_KEY = "AIzaSyDCv38dyT92Kalge4L8ibzHFVcLgvtps9Q"
url = "https://language.googleapis.com/v1/documents:analyzeEntities?key=" + API_KEY


raw_tx = "Software engineer, Google, Mountainview California, June 2022 - Present"

data = {
     "document": {
        object({
            "type": enum(PLAIN_TEXT),
            "language": string,

            # Union field source can be only one of the following:
            "content": string,
            # End of list of possible types for union field source.
        })
      },
      "encodingType": enum(UTF8),
}


# payload = urllib.urlencode({
#     "rawtx": raw_tx
#  })
#
result = urlfetch.fetch(url,
     method=urlfetch.POST,
     payload=data
)

if result.status_code == 200:
    j = json.loads(result.content)
    txid = j.get('txid')
    print txid, raw_tx
else:
    msg = 'Error accessing insight API:'+str(result.status_code)+" "+str(result.content)
    print msg

class MainPage(webapp2.RequestHandler):
    def get(self):
        pass



# #r = requests.post(url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/output?parameters", data = data)
# r = url.fetch("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyA7Uo226eyoZjz2H2gQh2eY-pgR5PzbES8")
#
#
# print(response)
# content = response.content
#
# json_result = json.loads(response.content)
# print(json_result)


app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug = True)
