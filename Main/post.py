import urllib.request
from comments import Comment, CommentList
from bs4 import BeautifulSoup
import datetime
import random
import re

class Post(object):
    """This class is for the Post objects

        Attributes:
            title: A String object that holds the title of the post
            numberOfComments: is an integer that holds the amount of comments made in
                      the post
            timeSubmitted: a datetime object that tracks the date and time the
                           post was created
            link: A string that holds the link to the comments of the post

    """

    def __init__(self,title,user,numberOfComments,timeSubmitted, link, commentsLink):
        self.title = title
        self.user = user
        self.numberOfComments = numberOfComments
        self.timeSubmitted = timeSubmitted
        self.link = link
        self.commentsLink = commentsLink
        self.comments = CommentList()

    def toString(self):
        """
        This function turns the object into a readable string
        Args:
            self: current instance of object
        Returns:
            str: String that displays the object's infromation
        """
        return(str(self.title)+ ' ' + str(self.user) + ' ' + str(self.numberOfComments))




class PostList(object):
    """This is a class that will run queries on Posts objects

        Attributes:
            posts: An array that holds all Post objects
            size: The amount of posts inside the array
            search: String that holds the search query for this postlist

    """

    def __init__(self,search, posts = []):
        self.search = search
        self.posts = posts
        self.size = len(posts)

    def add(self, post):
        self.posts.append(post)


    def addFromList(self, postList):
        self.posts.extend(postList.posts)