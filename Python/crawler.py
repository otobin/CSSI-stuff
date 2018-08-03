#!/usr/bin/Python
import urllib2
import time


print("Hello, World")
url = "http://www.example.com"


def fetch(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html


def get_anchors(html):

    a_start = 0
    a_end = -5
    anchors = []
    while True:
        a_start = html.find("<a ", a_end + 5)
        if a_start  == -1:
            break
        a_end = html.find("</a>", a_start+3)
        if a_end == -1:
            break
        anchor = html[a_start: a_end + 4]
        anchors.append(anchor)
    return anchors

def get_url(anchor):
    href_start = anchor.find('href="')
    href_end = anchor.find('"', href_start+6)
    url = anchor[href_start + 6: href_end]
    print url
    return url



def get_links(html):
    links = []
    #extract get_links
    anchors = get_anchors(html)
    for anchor in anchors:
        url = get_url(anchor)
        links.append(url)
    return links

urls_visited = []
urls_to_visit = []
urls_to_visit.append("http://matthewlevine.com/")

while len(urls_to_visit)>0:
    time.sleep(1)
    url = urls_to_visit.pop()
    print("Visiting " + url)
    if (url in urls_visited):
        continue  #continue exits the iteration and goes back to the top of the loop
    urls_visited.append(url)
    html = fetch(url)
    links = get_links(html)
    print ("Got %s links." %(len(links)))
    for link in links:
        urls_to_visit.append(link)
    #print(html)
