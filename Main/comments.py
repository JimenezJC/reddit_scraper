import urllib.request
from post import PostList, Post
from bs4 import BeautifulSoup
import datetime
import random
import re

class Comment(object):
    """ Class for the Comment Object

        Attributes:
            user = A string that shows the name of the user posting the comment
            content = A string that shows the content of the comment
            upvotes = An intenger that shows the amount of upvotes/downvotes

    """
    def __init__(self,user, content, score):
        self.user = user
        self.content = content
        self.score = score


class CommentList(object):
    """ Class that will be used to run queries on all Comment objects

        Attributes:
            comments = a list that will hold all comments objects
            size = the size of the comments list
    """
    def __init__(self, comments = []):
        self.comments = comments
        self.size = len(comments)

    def add(self, comment):
        self.comments.append(comment)
