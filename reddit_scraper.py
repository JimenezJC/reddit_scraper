import urllib.request
from bs4 import BeautifulSoup
import datetime
import random
import re



class Post(object):
    def __init__(self,title,user,comments,topic,timeSubmitted, link, clink):
        self.title = title
        self.comments = comments
        self.topic = topic
        self.timeSubmitted = timeSubmitted
        self.link = link
        self.clink = clink


def findPosts(searchUrl):
    
    url = ("https://www.reddit.com/r/streetwearstartup/search?q=lol&restrict_sr=on&sort=new&t=year" + searchUrl)
    req = urllib.request.Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    bsObj = BeautifulSoup(html,'lxml')
    posts = []
    for link in bsObj.findAll("div",{"class":"linkflair-designfeedback"}):
        title = link.div.a.text
        topic = "Design Feedback"
        postLink = link.a.get('href')
        comments = link.div.div.a.text[:-8]
        commentLink = link.div.div.a.get('href')
        user = link.div.div.find("span",{"class":"search-author"}).text[3:]
        timeSubmitted = link.div.div.find("span",{"class":"search-time"}).text[10:]
        post = Post(title, user, comments, topic, timeSubmitted, postLink, commentLink)
        posts.append(post)

    for link in bsObj.findAll("div",{"class":"linkflair-brandfeedback"}):
        title = link.div.a.text
        topic = "Brand Feedback"
        postLink = link.a.get('href')
        comments = link.div.div.a.text[:-8]
        commentLink = link.div.div.a.get('href')
        user = link.div.div.find("span",{"class":"search-author"}).text[3:]
        timeSubmitted = link.div.div.find("span",{"class":"search-time"}).text[10:]
        post = Post(title, user, comments, topic, timeSubmitted, postLink, commentLink)
        posts.append(post)

    for link in bsObj.findAll("div",{"class":"linkflair-showcase"}):
        title = link.div.a.text
        topic = "Showcase"
        postLink = link.a.get('href')
        comments = link.div.div.a.text[:-8]
        commentLink = link.div.div.a.get('href')
        user = link.div.div.find("span",{"class":"search-author"}).text[3:]
        timeSubmitted = link.div.div.find("span",{"class":"search-time"}).text[10:]
        post = Post(title, user, comments, topic, timeSubmitted, postLink, commentLink)
        posts.append(post)



    footer = bsObj.find("footer")
    for i in footer.findAll("a"):
        if(i.text == "next ›"):
            print(i.get('href')[83:])
            morePosts = findPosts((i.get('href')[83:]))
            posts.extend(morePosts)
        else:
            continue
    return posts

x = findPosts("")
for post in x:
    print(post.clink)
