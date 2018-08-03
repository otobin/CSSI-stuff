
import json
import requests
API_KEY = "AIzaSyA7Uo226eyoZjz2H2gQh2eY-pgR5PzbES8"


data = {
    "key": "AIzaSyA7Uo226eyoZjz2H2gQh2eY-pgR5PzbES8",
    "input": "California Academy of Sciences",
    "inputtype": "textquery"
}

# #r = requests.post(url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/output?parameters", data = data)
# r = url.fetch("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyA7Uo226eyoZjz2H2gQh2eY-pgR5PzbES8")
#
#
# print(response)
# content = response.content
#
# json_result = json.loads(response.content)
# print(json_result)

response = requests.post(url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyA7Uo226eyoZjz2H2gQh2eY-pgR5PzbES8")

print(response)
print(response.text)
