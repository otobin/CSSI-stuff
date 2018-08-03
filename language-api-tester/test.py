{u'entities':[ # entities

    {u'name': u'Google', u'salience': 0.5345132, u'metadata': {u'mid': u'/m/045c7b', u'wikipedia_url': u'https://en.wikipedia.org/wiki/Google'}, u'mentions': [{u'text': {u'beginOffset': 0, u'content': u'Google'}, u'type': u'PROPER'}], u'type': u'ORGANIZATION'},

    {u'name': u'software engineers', u'salience': 0.23102836, u'metadata': {}, u'mentions': [{u'text': {u'beginOffset': 11, u'content': u'software engineers'}, u'type': u'COMMON'}], u'type': u'PERSON'},

    {u'name': u'Mountanview', u'salience': 0.13288432, u'metadata': {}, u'mentions': [{u'text': {u'beginOffset': 33, u'content': u'Mountanview'}, u'type': u'PROPER'}], u'type': u'OTHER'},

    {u'name': u'California', u'salience': 0.101574115, u'metadata': {u'mid': u'/m/01n7q', u'wikipedia_url': u'https://en.wikipedia.org/wiki/California'}, u'mentions': [{u'text': {u'beginOffset': 46, u'content': u'California'}, u'type': u'PROPER'}], u'type': u'LOCATION'}

], u'language': u'en'}



{u'sentences': [{ 'text': {u'content': u"You're a fucking moron", u'beginOffset': 0},
                u'sentiment': {u'magnitude': 0.9, u'score': -0.9}],
u'documentSentiment': {u'magnitude': 0.9, u'score': -0.9},
u'language': u'en'}


 {u'categories':
 [{
     u'confidence': 0.69, u'name': u'/Science/Computer Science'}, {u'confidence': 0.57, u'name': u'/Computers & Electronics/Programming'}]}

j = dictionary =>
    entities = list =>
        more dictionaries (name, type[proper/common], type[category])



#functional getCategories
def getCategories(url): #url is unique to categories function in api
    data = {
     "document": {
        "type": "PLAIN_TEXT",
        "language": "EN",
        "content": "Google, headquartered in Mountain View, unveiled the new Android phone at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones."
      }
    }
    headers = {
    "Content-Type" : "application/json; charset=utf-8"
    }
    jsondata = json.dumps(data)
    result = urlfetch.fetch(url, method=urlfetch.POST, payload=data,headers=headers)
    python_result = json.loads(result.content)
    string = ""
    for i in range(0, len(python_result["categories"])):
         string += "Your resume indicates the "
         string += python_result["categories"][i]["name"]
         string += " category with a "
         string += str(python_result["categories"][i]["confidence"])
         string += " level of confidence. \n"
    return string
print(getCategories(url))




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
