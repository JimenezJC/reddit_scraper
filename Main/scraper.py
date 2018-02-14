import datetime
import random
import re
import urllib.request
import csv

from bs4 import BeautifulSoup

from comments import Comment, CommentList
from post import Post, PostList


class Scraper(object):
    """ Class for Scraper object which will scrape reddit.com
        Attributes:
            mainURL: the url that will be used as the inception of the search
            subReddit: optional search paramater where the mainURL will be decided
            library: the mini database that wll be used to store all the data goten
                     from the scraping. we will then be able to run data queries on
                     them.
            latestSearch: a string that holds the latest search query sent by the user
    """
    def __init__(self, subReddit=None):
        self.mainURL = "reddit.com"
        self.subReddit = subReddit
        self.library = []
        self.latestSearch = None


    def turnToCSV(self):
        """
        This function turns the library dataset into a CSV file
        Args:
            self: current instance of the object
        Returns:
            nothing, but it will create a file a csv file for the user and put it in a
            folder in document.
        """
        with open(self.latestSearch + '_posts.csv', 'wb') as csvfile:
            rwriter = csv.writer(csvfile, delimiter=',',
                                          quotechar='|',
                                          quoting=csv.QUOTE_MINIMAL
                                          )
            for post in self.library[0].posts:
                rwiter.writerow([post.title,
                                 post.user,
                                 post.numberOfComments,
                                 post.timeSubmitted,
                                 post.link,
                                 post.commentsLink,
                                 ])

        with open(self.latestSearch + '_comments.csv', 'wb') as csvfile:
            rwriter = csv.writer(csvfile, delimiter=',',
                                          quotechar='|',
                                          quoting=csv.QUOTE_MINIMAL
                                          )
            for comment in self.library[1].comments:
                rwriter.writerow([comment.user,
                                  comment.content,
                                  comment.score])




    def printResults(self):
        """
        This functions prints the most recent search done using the scraper
        Args:
            self: the current instance of the object
        Returns:
            nothing, only prints out the scrape results in a readable format.
            turning the latest scrape into a csv is an option however.
        """
        for i in range(len(self.library)):
            if(i == 0):
                print('posts')
                for post in self.library[i].posts:
                    print(post.toString())
            else:
                print('comments')
                for comment in self.library[i].comments:
                    print(comment.toString())


    def clear(self):
        """
        This function clears out the library attribute of the scraper object
        Args:
            self: current instance of the object
        Return:
            nothing, just clears out the library attribute
        """
        del self.library[:]


    def scrape(self, search):
        """
        This function scrapes reddit search for posts and comments based off the search input
        given by the user
        Args:
            self: current instance of the objectz
            search: a string that is given by the user. this string will be our main
                    search term when scraping
        Returns:
            nothing, but the library array will be filled with a postLists object, as well as a
            commentsList object.
        """
        self.latestSearch = search
        postsList = self.scrapePosts(search)
        self.library.append(postsList)
        comments = self.scrapeComments(postsList)
        self.library.append(comments)


    def scrapePosts(self, search, extended=""):
        """
        This function uses beautifulsoup4 to create a bsObj which we can then use to scrape
        for information. The function is recursive and will continue to search reddit pages
        until none are left.
        Args:
            self: current instance of the object
            search: a string that is given by the user and is the main arguement for our search
                    query
            extended: the extended link, is defaulted to none for our base-case and is used
                      for every recursive call after.
        Returns:
            posts: a postLists object that contains all the post objects.
                   we return this for the recursive loop as well to give it back to the original
                   "scrape" function.
        """
        if self.subReddit == None:
            baseUrl = ("https://www.reddit.com/search?q=" + search + extended)
        else:
                        baseUrl = ("https://www.reddit.com/r/"+ self.subReddit +"/search?q="+ search +"&restrict_sr=on&sort=relevance&t=all" + extended)
        req = urllib.request.Request(baseUrl, headers = {'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        bsObj = BeautifulSoup(html, 'lxml')
        posts = PostList(search)
        for link in bsObj.findAll("div", {"class": "no-linkflair"}):
            title = link.div.a.text
            postLink = link.a.get('href')
            comments = link.div.div.a.text[:-8]
            commentLink = link.div.div.a.get('href')
            user = link.div.div.find("span", {"class":"search-author"}).text[3:]
            timeSubmitted = link.div.div.find("span",{"class":"search-time"}).text[10:]
            post = Post(title, user, comments,timeSubmitted,postLink, commentLink)
            posts.add(post)
        footer = bsObj.find("footer")
        for i in footer.findAll("a"):
            if(i.text == "next ,"):
                print(i.get('href')[83:])
                morePosts = self.scrapePosts(search,(i.get('href')[83:]))
                posts.addFromList(morePosts)
            else:
                continue
        return posts

    def scrapeComments(self,postList):
        """
        This function uses the bsObj gotten from BeautifulSoup4 to get
        all the comment information from the threads we scraped in the
        scrapePosts
        Args:
            self: current instance of the scraper object
            postList: a postList object containing all the posts just created
        Returns:
            comments: a commentList object that contains all the comments
                      objects we just scraped.
        """
        comments = CommentList()
        for post in postList.posts:
            commentLink = post.commentsLink
            req = urllib.request.Request(commentLink, headers = {'User-Agent':'Mozilla/5.0'})
            html = urllib.request.urlopen(req).read()
            bsObj = BeautifulSoup(html, 'lxml')
            for comm in bsObj.findAll("div", {"class":"entry"})[1:]:
                print('lol')
                print(comm.p.prettify())
                user = comm.p.findAll("a")[1].text
                score = comm.p.findAll("span")[3].text[:-6]
                post = comm.div.div.text
                comment = Comment(user, post, score)
                comments.add(comment)
        return comments
